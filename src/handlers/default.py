from aiogram import Router, types
from src.modules.functions import check_user_registered


default_router = Router()


@default_router.message()
async def echo_handler(message: types.Message) -> None:
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return
    await message.answer("Извините, у меня лапки!")