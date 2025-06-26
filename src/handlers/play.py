import asyncio
import random

import aiosqlite
from aiogram.types import ReplyKeyboardRemove

from src.modules.admin import DB_PATH
from src.modules.constants import goodbyes, FANTIK_REACTIONS, SPECIAL_EVENTS
from src.modules.functions import check_user_registered, get_notification_status
from aiogram import Router, F, types

from src.modules.keyboards import create_main_keyboard, create_game_keyboard

play_router = Router()


@play_router.message(F.text == 'Бегать за фантиком')
async def play(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return

    await message.answer(
        "🐱 Ура-а-а! *приносит фантик* "
        "Давай поиграем! Кидай мне его, а я буду приносить его обратно!",
        reply_markup=create_game_keyboard()
    )


@play_router.message(F.text == 'Бросить фантик')
async def fantik(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return

    # С вероятностью 25% особое событие
    if random.random() < 0.25:
        event_type = random.choice(list(SPECIAL_EVENTS.keys()))
        response = random.choice(SPECIAL_EVENTS[event_type])

        if event_type == "fantik_lost":
            await message.answer(response)
            await asyncio.sleep(1)
            await message.answer_sticker("CAACAgIAAxkBAAEPo2NoQWsJhI0JBXxHYIhVbdG9tlMlTAACPnIAAnxAuEkLUfaBTwYcIDYE")  # ID стикера с грустным котом
            return
        else:
            await message.answer(response)
            await asyncio.sleep(1)
            return

    # Обычная реакция
    response = random.choice(FANTIK_REACTIONS)

    await message.answer(response)


@play_router.message(F.text == 'Закончить игру')
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
        f"{random.choice(goodbyes)}\n\nВот что я могу:",
        reply_markup=create_main_keyboard(current_status)
    )