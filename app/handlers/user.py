from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Здравствуйте, это бот записывает вас в очередь в сервисный центр\nВы можнте узнать о нас и наших услугах, оставить завку на ремонт и следить за статусом заявки")