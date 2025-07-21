from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

service_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Оставить заявку'), KeyboardButton(text="Статус ремонта")],
        [KeyboardButton(text='Контакты'), KeyboardButton(text='Услуги и цены')]
    ],
    resize_keyboard=True)