import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from modules.logger import logger

# Импорты роутеров
from src.handlers.belly_rub import belly_rub_router
from src.handlers.currency_exchange import currency_exchange_router
from src.handlers.default import default_router
from src.handlers.notifications import notifications_router
from src.handlers.play import play_router
from src.handlers.send_murmontik_sticker import send_murmontik_sticker_router
from src.handlers.start import on_startup, on_shutdown, start_router
from src.handlers.stop_bot import stop_bot_router
from src.handlers.tygydyk import tygydyk_router


async def main() -> None:
    start_time = datetime.now()
    logger.info("Initializing bot...")

    # Загрузка конфигурации
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("BOT_TOKEN not found in environment variables")
        return

    # Инициализация бота и диспетчера
    dp = Dispatcher()
    bot = Bot(token)

    try:
        # Регистрируем обработчики startup/shutdown
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)

        # Порядок важен: от специфичных к общим
        routers = [
            start_router,
            stop_bot_router,
            notifications_router,
            currency_exchange_router,
            play_router,
            tygydyk_router,
            belly_rub_router,
            send_murmontik_sticker_router,
            default_router  # Должен быть последним!
        ]

        for router in routers:
            dp.include_router(router)

        logger.info(f"Starting bot with {len(routers)} routers...")
        await dp.start_polling(bot)

    except asyncio.CancelledError:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.exception(f"Bot crashed: {e}")
    finally:
        await bot.session.close()
        logger.info(f"Bot stopped. Uptime: {datetime.now() - start_time}")

if __name__ == "__main__":
    asyncio.run(main())
