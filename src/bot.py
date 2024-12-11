import datetime

from aiogram import Bot, Dispatcher, html
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
            notification_text += f"{html.bold(chat_name)}\n\n" if chat_name else "\n"

            # Информация об отправителе
            if message.from_user:
                notification_text += f"От: {message.from_user.full_name} "
                if message.from_user.username:
                    notification_text += f"(@{message.from_user.username})"
                notification_text += "\n\n"

            # Текст сообщения
            notification_text += f"\n{message.text or message.caption or 'Сообщение без текста'}"

            # Ссылка на чат
            invite = await self.bot.create_chat_invite_link(
                chat_id=message.chat.id,
                expire_date= datetime.datetime.now() + datetime.timedelta(days=2),
                member_limit=1
            )
            notification_text += f"\n\n{html.link(f"Перейти к чату {chat_name}", invite.invite_link)}"


            # Отправляем уведомление
            await self.bot.send_message(
                chat_id=user_id,
                text=notification_text,
                parse_mode="HTML"
            )

        except Exception as e:
            # Логируем ошибки отправки
            print(f"Ошибка отправки уведомления: {e}")