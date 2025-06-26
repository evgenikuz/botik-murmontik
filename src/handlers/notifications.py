import asyncio

import aiosqlite

from src.modules.admin import DB_PATH
from src.modules.functions import check_user_registered, get_notification_status, set_notification_status, \
    set_work_schedule, is_working_day
from src.modules.keyboards import create_main_keyboard, get_schedule_keyboard
from src.modules.logger import logger
from aiogram import Router, F, types, Bot
from datetime import datetime, time


notifications_router = Router()


@notifications_router.message(F.text.in_(['Напоминать о дейли и списании времени',
                                              'Отключить напоминания о дейли и списании времени']))
async def toggle_reminders(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return

    user_id = message.from_user.id
    current_status = await get_notification_status(user_id)

    if current_status:
        # Отключаем уведомления
        await set_notification_status(user_id, False)
        await set_work_schedule(user_id, None)  # Сбрасываем график

        kb = create_main_keyboard(False)
        await message.answer(
            'Напоминания отключены!',
            reply_markup=kb
        )
    else:
        # Спрашиваем график работы
        await ask_work_schedule(message)


async def ask_work_schedule(message: types.Message):
    """Спрашиваем график работы пользователя"""
    keyboard = get_schedule_keyboard()
    await message.answer(
        "Выберите ваш график работы:",
        reply_markup=keyboard
    )


@notifications_router.callback_query(F.data.startswith("schedule_"))
async def process_schedule(callback: types.CallbackQuery):
    """Обрабатываем выбор графика работы"""
    user_id = callback.from_user.id
    schedule_type = callback.data

    # Сохраняем график в БД и включаем уведомления
    await set_work_schedule(user_id, schedule_type)
    await set_notification_status(user_id, True)

    # Формируем красивое название графика
    schedule = schedule_type.replace("schedule_", "").replace("_", "-")

    # Обновляем клавиатуру
    kb = create_main_keyboard(True)

    await callback.message.answer(
        f"Отлично! Буду напоминать согласно графику {schedule}",
        reply_markup=kb
    )
    await callback.answer()


async def send_reminder(user_id: int, text: str):
    """Отправка напоминания конкретному пользователю"""
    try:
        bot = get_bot_instance()  # Получаем инициализированный бот
        print("дошли до отправки")
        print(bot_instance)
        if bot_instance:
            print("если бот инстанс")
            await bot.send_message(user_id, text)
    except Exception as e:
        logger.error(f"Error sending reminder to user {user_id}: {e}")


async def check_and_send_reminders(bot: Bot):
    """Функция для проверки и отправки напоминаний всем пользователям"""
    while True:
        try:
            now = datetime.now()
            current_time = now.time()

            if not is_working_day(now):
                await asyncio.sleep(6 * 3600)
                continue

            users = await get_users_with_notifications()

            for user_id, schedule_type in users:
                await process_user_schedule(bot, user_id, schedule_type, current_time)

            await asyncio.sleep(60)

        except asyncio.CancelledError:
            logger.info("Reminder task cancelled")
            break
        except Exception as e:
            logger.error(f"Error in reminder task: {e}")
            await asyncio.sleep(60)


async def get_users_with_notifications() -> list:
    """Получает пользователей с активными уведомлениями"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            '''SELECT user_id, work_schedule 
               FROM users 
               WHERE receives_notifications = 1 AND work_schedule IS NOT NULL'''
        )
        users = await cursor.fetchall()
        await cursor.close()
    return users


async def process_user_schedule(bot: Bot, user_id: int, schedule_type: str, current_time: time):
    """Обрабатывает уведомления по расписанию пользователя"""
    try:
        if schedule_type == "schedule_9_18":
            if time(9, 0) <= current_time < time(9, 1):
                await bot.send_message(user_id, 'Доброе утро! Начинаем рабочий день! 🌞')
            elif time(11, 58) <= current_time < time(11, 59):
                await bot.send_message(user_id, 'А вот и я! Помнишь про дейлик? 🤓')
            elif time(13, 0) <= current_time < time(13, 1):
                await bot.send_message(
                    user_id,
                    'Время обеда! Не забудь списать трудозатраты в Jira и '
                    'прокомментировать задачки!'
                )
            elif time(17, 50) <= current_time < time(17, 51):
                await bot.send_message(
                    user_id,
                    'Мяу! На сегодня всё! Не забудь списать трудозатраты в Jira '
                    'и прокомментировать задачки. Пока!'
                )

        elif schedule_type == "schedule_10_19":
            if time(10, 0) <= current_time < time(10, 1):
                await bot.send_message(user_id, 'Доброе утро! Начинаем рабочий день! 🌞')
            elif time(11, 58) <= current_time < time(11, 59):
                await bot.send_message(user_id, 'А вот и я! Помнишь про дейлик? 🤓')
            elif time(14, 0) <= current_time < time(14, 1):
                await bot.send_message(
                    user_id,
                    'Время обеда! Не забудь списать трудозатраты в Jira и '
                    'прокомментировать задачки!'
                )
            elif time(18, 50) <= current_time < time(18, 51):
                await bot.send_message(
                    user_id,
                    'Мяу! На сегодня всё! Не забудь списать трудозатраты в Jira '
                    'и прокомментировать задачки. Пока!'
                )
    except Exception as e:
        logger.error(f"Failed to send message to user {user_id}: {e}")

