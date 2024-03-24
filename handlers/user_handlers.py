from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def proces_start_command(message: Message):
    """ Реакция на команду /start. """
    await message.answer(text=LEXICON_RU['/start'])
