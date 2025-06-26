import asyncio

from src.modules.functions import check_user_registered
from src.modules.logger import logger
from aiogram import Router, F, types
from src.modules.constants import MURMONTIK_STICKERS
import random

send_murmontik_sticker_router = Router()


@send_murmontik_sticker_router.message(F.text == 'Прислать своё фото')
async def send_murmontik_sticker(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return

    try:
        # Выбираем случайный стикер
        random_sticker = random.choice(MURMONTIK_STICKERS)
        await asyncio.sleep(1)
        await message.answer_sticker(random_sticker)
        await message.answer("Вот моё лучшее фото!")
    except Exception as e:
        logger.error(f"Error sending sticker: {e}")
        await message.answer("Ой, не могу найти фото... Попробуй позже!")