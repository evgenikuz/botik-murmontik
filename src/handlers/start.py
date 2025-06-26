import asyncio
from random import random

import aiosqlite
from aiogram.types import ReplyKeyboardRemove

from src.modules.admin import DB_PATH
from src.modules.functions import add_user, get_notification_status
from aiogram import Router, types, Bot, F
from aiogram.filters import Command

from src.modules.keyboards import create_main_keyboard
from src.modules.logger import logger

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    await add_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username
    )

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(text='Кис-кис')]
    ])
    await message.answer("Пиу пиу пиу пиу тррр тррр тррр")
    await asyncio.sleep(3)
    await message.reply(
        'Я запустился! Позови меня, чтобы узнать, что я умею',
        reply_markup=kb
    )


@start_router.message(F.text.lower() == 'кис-кис')
@start_router.message(F.text.lower() == 'кис кис')
async def menu(message: types.Message):
    user_id = message.from_user.id

    # Проверяем, существует ли пользователь в БД
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT 1 FROM users WHERE user_id = ?', (user_id,))
        exists = await cursor.fetchone()
        await cursor.close()

    if not exists:
        await message.answer(
            "Пожалуйста, начни общение со мной с помощью команды /start",
            reply_markup=ReplyKeyboardRemove()
        )
        return

    current_status = await get_notification_status(user_id)

    await message.answer(
        f"Вот что я могу:",
        reply_markup=create_main_keyboard(current_status)
    )


async def on_startup(bot: Bot):
    """Функция, выполняемая при запуске бота"""
    from .notifications import check_and_send_reminders
    asyncio.create_task(check_and_send_reminders(bot))


async def on_shutdown(bot: Bot):
    """Функция, выполняемая при выключении бота"""
    logger.info("Bot stopped")
