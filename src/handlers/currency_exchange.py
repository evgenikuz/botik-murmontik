import random
import asyncio

from src.modules.functions import check_user_registered
from src.modules.logger import logger
from aiogram import Router, F, types
from src.modules.constants import DEFAULT_RATES, MONGE_PRICE

currency_exchange_router = Router()


@currency_exchange_router.message(F.text == 'Рассказать о курсе валют')
async def currency_exchange(message: types.Message):
    if not await check_user_registered(message.from_user.id):
        await message.answer("Пожалуйста, начни общение со мной с помощью команды /start")
        return

    try:
        # Выбираем случайную валюту
        currency, rate = random.choice(list(DEFAULT_RATES.items()))

        # Рассчитываем цену за 1 грамм
        price_per_gram = MONGE_PRICE / 10000

        # Сколько грамм можно купить за 1 единицу валюты
        grams_per_unit = (1 * rate) / price_per_gram

        # Показываем пользователю, что идет расчет
        await message.answer("🐱 Считаю коричневые камушки...")
        await asyncio.sleep(2)

        # Формируем ответ
        response = (
            f"За 1 {currency} можно купить {grams_per_unit:.1f} г камушков Monge для кошек\n\n"
            f"<i>Курсы обновляются вручную, потому что у меня лапки</i>"
        )

        await message.answer(response, parse_mode="HTML")

    except Exception as e:
        logger.error(f"Error in currency exchange: {e}")
        await message.answer("Извините, я где-то ошибся и не смог посчитать")