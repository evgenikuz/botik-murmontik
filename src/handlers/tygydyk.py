import asyncio
from random import choice

from aiogram.types import ReplyKeyboardRemove

from src.modules.constants import DAY_EXCUSES, NIGHT_REACTIONS
from src.modules.functions import is_night_time, get_notification_status
from src.modules.functions import check_user_registered
from aiogram import Router, F, types

from src.modules.keyboards import create_main_keyboard

tygydyk_router = Router()


@tygydyk_router.message(F.text == 'Тыгыдыкать ночью')
async def tygydyk(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return


    user_id = message.from_user.id
    current_status = await get_notification_status(user_id)

    if is_night_time():
        # Ночная безумная активность
        response = choice(NIGHT_REACTIONS)

        # С вероятностью 20% "порча" интерфейса
        if choice(range(10)) < 2:
            await message.answer(
                response,
                reply_markup=ReplyKeyboardRemove()
            )
            await message.answer(
                "*кот наступил на клавиатуру*\n"
                "Подождите, временные неполадки с клавиатурой..."
            )
            await asyncio.sleep(5)
            await message.answer(
                "Всё, я исправил!",
                reply_markup=create_main_keyboard(current_status)
            )
        else:
            await message.answer(response)
    else:
        # Дневная лень
        excuse = choice(DAY_EXCUSES)

        # Иногда добавляем картинку спящего кота
        if choice(range(10)) < 4:
            await message.answer_sticker(
                "CAACAgIAAxkBAAEPoyNoQWriWmLcodqsy0H1YS6yZN8MRwACu3QAAnDNuUlbXYQSAAELzVQ2BA",  # Вставьте ID фото спящего кота
            )
            await message.answer(excuse)
        else:
            await message.answer(excuse)

