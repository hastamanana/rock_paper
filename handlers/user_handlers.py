from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from lexicon.lexicon import LEXICON, LEXICON_GAME
from keyboards.keyboards import rock_paper_scissors_btn, yes_no_help
from services.services import get_bot_choice, get_winner

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON['start'], 
                    reply_markup=yes_no_help)


@router.message(F.text == 'Давай сыграем')
async def start_game(message: Message):
    await message.answer(text=LEXICON['play'], 
                   reply_markup=rock_paper_scissors_btn.as_markup(resize_keyboard=True))
    
@router.message(F.text == 'Не хочу играть')
async def no_play(message: Message):
    await message.answer(f"Хорошо. Если, вдруг, захочешь сыграть "
                         "- нажми 'Давай сыграем!'"
                         )
    
@router.message(F.text.in_([LEXICON_GAME['rock'],
                            LEXICON_GAME['paper'],
                            LEXICON_GAME['scissors']]))
async def game_buttons(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f"Мой выбор: {LEXICON_GAME[bot_choice]}" )
    winner = get_winner(message.text, bot_choice, LEXICON_GAME)
    if winner == LEXICON_GAME['user_won']:
        winner = winner.format(message.from_user.full_name)
    print(winner)
    await message.answer(text=winner+'\n\nХотите сыграть еще?', reply_markup=yes_no_help)


@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(text=LEXICON['help'])