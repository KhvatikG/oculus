from typing import List, Optional
from functools import partial

from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Filter

from src.config import settings
from src.bot import OculusBot  # Импортируем базовый класс бота

class MentionFilter(Filter):
    """
    Кастомный фильтр для детектирования упоминаний
    """
    def __init__(self, usernames: Optional[List[str]] = None):
        self.usernames = usernames or []

    async def __call__(self, message: Message) -> bool:
        if not message.text:
            return False

        # Проверка прямого упоминания через @username
        if any(f'@{username}' in message.text for username in self.usernames):
            return True

        # Проверка упоминания по имени
        if any(username.lower() in message.text.lower() for username in self.usernames):
            return True

        return False

async def handle_mention(message: Message, bot: OculusBot):
    """
    Обработчик сообщений с упоминаниями
    """
    if message.from_user:
        for admin_id in settings.ADMIN_IDS:
            # Получаем название чата
            chat_name = message.chat.title if message.chat.title else "Неизвестный чат"

            # Отправляем уведомление через метод бота
            await bot.send_mention_notification(
                user_id=admin_id,
                message=message,
                chat_name=chat_name
            )

def register_mention_handlers(dp: Dispatcher, bot: OculusBot):
    """
    Регистрация обработчиков упоминаний
    """
    mention_filter = MentionFilter(usernames=[settings.USERNAME])
    dp.message.register(partial(handle_mention, bot=bot), mention_filter)