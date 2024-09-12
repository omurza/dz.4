from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

buttons1 = [
    [KeyboardButton(text="Geeks"), KeyboardButton(text="Направления")]
]
keyboard1 = ReplyKeyboardMarkup(keyboard=buttons1, resize_keyboard=True)

inline1 = [
    [InlineKeyboardButton(text="backend", callback_data='backend')],
    [InlineKeyboardButton(text="frontend", callback_data='frontend')],
    [InlineKeyboardButton(text="UX/UI", callback_data='dizain')],
    [InlineKeyboardButton(text="android", callback_data='android')]
]
inline2 = InlineKeyboardMarkup(inline_keyboard=inline1)

geeks_inline = [
    [InlineKeyboardButton(text="o Geeks.pro", url="https://geeks.kg/geeks-pro")],
    [InlineKeyboardButton(text="o Geeks студио", url="https://geekstudio.kg/")],
    [InlineKeyboardButton(text="o главном сайте Geeks", url="https://geeks.kg/")]
]

geeks_keyboard = InlineKeyboardMarkup(inline_keyboard=geeks_inline)
backend_inline = [
    [InlineKeyboardButton(text="django", callback_data='DJ')],
    [InlineKeyboardButton(text="python", callback_data='pyt')],
    [InlineKeyboardButton(text="aiogram", callback_data='AIO')],
]
inline434 = InlineKeyboardMarkup(inline_keyboard=backend_inline)
frontend_inline = [
    [InlineKeyboardButton(text="HTML", callback_data='HTML')],
    [InlineKeyboardButton(text="JS", callback_data='JS')],
    [InlineKeyboardButton(text="CSS", callback_data='CSS')],
]
inline443 = InlineKeyboardMarkup(inline_keyboard=frontend_inline)
android_inline = [
    [InlineKeyboardButton(text="приложения", callback_data='WEB')],
    [InlineKeyboardButton(text="защита", callback_data='SEC')],
    [InlineKeyboardButton(text="ПО", callback_data='PO')],
]
inline431 = InlineKeyboardMarkup(inline_keyboard=android_inline)
dizain_inline = [
    [InlineKeyboardButton(text="UI_Design", callback_data='UI')],
    [InlineKeyboardButton(text="UX_Design", callback_data='UX')],
    [InlineKeyboardButton(text="web_desin", callback_data='web')],
]
inline432 = InlineKeyboardMarkup(inline_keyboard=dizain_inline)