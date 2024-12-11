from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


async def start_command(message: Message):
    """
    Обработчик команды /start
    """
    await message.answer(
        "👋 Привет! Я Oculus - бот для отслеживания упоминаний.\n\n"
        "Добавь меня в групповой чат, и я буду присылать тебе "
        "уведомления, когда тебя упомянут."
    )


async def help_command(message: Message):
    """
    Обработчик команды /help
    """
    help_text = (
        "🤖 Помощь по боту Oculus:\n\n"
        "• Добавь меня в группу\n"
        "• Дай права администратора для корректной работы\n"
        "• Я буду присылать уведомления о упоминаниях\n\n"
        "Вопросы? Пиши @your_username"
    )
    await message.answer(help_text)


def register_system_handlers(dp: Dispatcher):
    """
    Регистрация системных обработчиков
    """
    dp.message.register(start_command, Command(commands=['start']))
    dp.message.register(help_command, Command(commands=['help']))