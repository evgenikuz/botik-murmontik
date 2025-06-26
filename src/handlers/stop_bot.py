import aiosqlite
from aiogram.types import ReplyKeyboardRemove

from src.modules.admin import DB_PATH
from src.modules.functions import check_user_registered
from aiogram import Router, F, types
from aiogram.filters import Command

stop_bot_router = Router()


@stop_bot_router.message(F.text == 'Остановить бот')
@stop_bot_router.message(Command("stop"))
async def stop_bot_handler(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return
    user_id = message.from_user.id

    # Удаляем пользователя из базы данных
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        await db.commit()

    # Отправляем прощальное сообщение
    await message.answer(
        "Бот остановлен. Все данные удалены.\n"
        "Если захочешь снова со мной пообщаться, используй команду /start",
        reply_markup=ReplyKeyboardRemove()
    )