from aiogram import Bot, Dispatcher
from aiogram.types import Message
from typing import Optional

from src.handlers.system import register_system_handlers
from src.handlers.mention import register_mention_handlers


class OculusBot:
    def __init__(self, bot: Bot, dp: Dispatcher):
        self.bot = bot
        self.dp = dp

    async def setup(self):
        """
        Настройка и регистрация основных обработчиков событий
        """

        # Регистрация системных хэндлеров
        register_system_handlers(self.dp)

        # Регистрация хэндлеров упоминаний
        register_mention_handlers(self.dp, self)

    async def send_mention_notification(
            self,
            user_id: int,
            message: Message,
            chat_name: Optional[str] = None
    ):
        """
        Отправка расширенного уведомления о упоминании
        """
        try:
            # Формируем подробное уведомление
            notification_text = f"🔔 Упоминание в чате "
            notification_text += f"*{chat_name}*\n\n" if chat_name else "\n"

            # Информация об отправителе
            if message.from_user:
                notification_text += f"От: {message.from_user.full_name} "
                if message.from_user.username:
                    notification_text += f"(@{message.from_user.username})"
                notification_text += "\n\n"

            # Текст сообщения
            notification_text += f"```\n{message.text or message.caption or 'Сообщение без текста'}```"

            # Кнопка перехода к сообщению
            if message.chat and message.message_id:
                notification_text += f"\n[Перейти к сообщению](https://t.me/c/{message.chat.id}/{message.message_id})"

            # Отправляем уведомление
            await self.bot.send_message(
                chat_id=user_id,
                text=notification_text,
                parse_mode='Markdown'
            )
        except Exception as e:
            # Логируем ошибки отправки
            print(f"Ошибка отправки уведомления: {e}")