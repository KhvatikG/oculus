import asyncio
import logging

from aiogram import Bot, Dispatcher
from src.config import settings
from src.bot import OculusBot

async def main():
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    # Инициализация бота и диспетчера
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    # Создание экземпляра нашего бота
    oculus_bot = OculusBot(bot, dp)

    # Регистрация хэндлеров
    await oculus_bot.setup()

    try:
        # Запуск поллинга
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())