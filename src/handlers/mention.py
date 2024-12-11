from aiogram import Dispatcher
from aiogram.types import Message
from src.config import settings


async def handle_mention(message: Message):
    """
    Обработчик сообщений с упоминаниями
    """
    # Проверяем, есть ли упоминание текущего пользователя
    # Здесь будет более сложная логика в следующих итерациях
    if message.from_user and message.from_user.id not in settings.ADMIN_IDS:
        # В текущей версии просто уведомляем администраторов
        for admin_id in settings.ADMIN_IDS:
            print(f"Mention for admin {admin_id}")
            # В реальной реализации будет вызов метода send_mention_notification


def register_mention_handlers(dp: Dispatcher):
    """
    Регистрация обработчиков упоминаний
    """
    # Placeholder для будущей более сложной логики
    dp.message.register(handle_mention)
