from aiogram import Bot, Dispatcher
from aiogram.types import Message
from typing import Optional


class OculusBot:
    def __init__(self, bot: Bot, dp: Dispatcher):
        self.bot = bot
        self.dp = dp

    async def setup(self):
        """
        Настройка и регистрация основных обработчиков событий
        """
        from src.handlers.system import register_system_handlers
        from src.handlers.mention import register_mention_handlers

        # Регистрация системных хэндлеров
        register_system_handlers(self.dp)

        # Регистрация хэндлеров упоминаний
        register_mention_handlers(self.dp)

    async def send_mention_notification(
            self,
            user_id: int,
            message: Message,
            chat_name: Optional[str] = None
    ):
        """
        Отправка уведомления о упоминании

        :param user_id: ID пользователя, которому отправляется уведомление
        :param message: Оригинальное сообщение с упоминанием
        :param chat_name: Название чата (опционально)
        """
        try:
            # Формируем текст уведомления
            notification_text = f"👀 Упоминание в чате "
            notification_text += f"*{chat_name}*\n\n" if chat_name else "\n"
            notification_text += f"```\n{message.text or message.caption or 'Сообщение без текста'}```"

            # Отправляем уведомление
            await self.bot.send_message(
                chat_id=user_id,
                text=notification_text,
                parse_mode='Markdown'
            )
        except Exception as e:
            # Логируем ошибки отправки
            print(f"Ошибка отправки уведомления: {e}")