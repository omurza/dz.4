from aiogram.types import Message , CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F, Router

from app.keyboards import *

router = Router()

@router.message(CommandStart())
async def start_of_aura(message: Message):
    await message.reply("Пиривет", reply_markup=keyboard1)

@router.message(F.text == "Geeks")
async def gre(message: Message):
    await message.reply("Компания Geeks — это ведущий игрок на рынке IT-услуг и решений. Мы специализируемся на разработке программного обеспечения, внедрении IT-инфраструктуры и предоставлении консалтинговых услуг, которые помогают бизнесу достигать новых высот."
                        , reply_markup=geeks_keyboard)

@router.message(F.text == "Направления")
async def dir(message: Message):
    await message.reply("Наши основные направления:", reply_markup=inline2)

@router.callback_query(F.data == "frontend")
async def diiуf(callback: CallbackQuery):
    await callback.message.answer(
        "фронтенд -это передняя чать сайтов все что вы видите делает фронтенд и абу ака:",
        reply_markup=inline443)  
@router.callback_query(F.data == "dizain")
async def ditуf(callback: CallbackQuery):
    await callback.message.answer(
        "Дизайн — это процесс создания визуального оформления и эстетики продуктов, который влияет на их функциональность и восприятие пользователями.",
        reply_markup=inline432)
@router.callback_query(F.data == "backend")
async def ddiуf(callback: CallbackQuery):
    await callback.message.answer(
        "Бэкенд — это задняя часть сайтов и приложений. Основные направления:",
        reply_markup=inline434)
@router.callback_query(F.data == "android")
async def ddiуf(callback: CallbackQuery):
    await callback.message.answer(
        "Андроид — это операционная система для мобильных устройств, разработанная Google, которая предоставляет гибкость и расширенные возможности для пользователей и разработчиков.:",
        reply_markup=inline431)


@router.callback_query(F.data == "AIO")
async def dd4iуf(callback: CallbackQuery):
    await callback.message.answer(
        "telegram->aiogram->python->мучения->telegrambot:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "DJ")
async def dd5iуf(callback: CallbackQuery):
    await callback.message.answer(
        "DJ или же Django это импортозамещение наш отечественый JavaScript:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "UI")
async def dd23iуf(callback: CallbackQuery):
    await callback.message.answer(
        " за красату в дизайне:",
        )    
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "UX")
async def dd4iуf(callback: CallbackQuery):
    await callback.message.answer(
        "за удобства в дизайне:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "web")
async def dd5iуf(callback: CallbackQuery):
    await callback.message.answer(
        "созадние обложки сайта:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "WEB")
async def dd23iуf(callback: CallbackQuery):
    await callback.message.answer(
        " разработка приложений:",
        )    
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "SEC")
async def dd4iуf(callback: CallbackQuery):
    await callback.message.answer(
        "создание защиты через андроид:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "PO")
async def dd5iуf(callback: CallbackQuery):
    await callback.message.answer(
        "програмное обеспечения на основе андройда:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "pyt")
async def dd23iуf(callback: CallbackQuery):
    await callback.message.answer(
        " самый популярный язык програмирования:",
        )    
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "HTML")
async def dd4iуf(callback: CallbackQuery):
    await callback.message.answer(
        "конструктор для началной создания сайтов:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "CSS")
async def dd5iуf(callback: CallbackQuery):
    await callback.message.answer(
        "вообще без понятия:",
        )
    await callback.answer('ну типа работает')
@router.callback_query(F.data == "JS")
async def dd23iуf(callback: CallbackQuery):
    await callback.message.answer(
        " ' язык програмирования для сайтов:",
        )    
    await callback.answer('ну типа работает')