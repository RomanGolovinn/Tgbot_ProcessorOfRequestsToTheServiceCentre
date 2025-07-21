from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.keyboards import service_keyboard

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Здравствуйте, это бот записывает вас в очередь в сервисный центр\n"
                         "Вы можнте узнать о нас и наших услугах, оставить завку на ремонт и следить за статусом заявки",
                         reply_markup=service_keyboard)