from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_NO_GAME

router = Router()


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_NO_GAME["other_answer"])
