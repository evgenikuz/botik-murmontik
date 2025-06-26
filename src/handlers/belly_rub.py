import asyncio

from src.modules.functions import check_user_registered
from src.modules.logger import logger
from aiogram import Router, F, types
from src.modules.constants import MURMONTIK_STICKERS, BELLY_RUB_RESPONSES
import random

belly_rub_router = Router()


@belly_rub_router.message(F.text == 'Погладить животик')
async def belly_rub(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return

    try:
        # Выбираем случайную реакцию
        response = random.choice(BELLY_RUB_RESPONSES)

        # Добавляем небольшую задержку для эффекта
        await message.answer("Идёт принятие решения относительно таких опрометчивых действий...")
        await asyncio.sleep(1)

        # Отправляем реакцию
        await message.answer(response)

        # С вероятностью 30% отправляем дополнительный стикер
        if random.random() < 0.3:
            await message.answer_sticker(random.choice(MURMONTIK_STICKERS))

    except Exception as e:
        logger.error(f"Error in belly rub: {e}")
        await message.answer("Мяяяу? *не понимает*")