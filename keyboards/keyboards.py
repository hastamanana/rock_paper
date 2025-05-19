from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

yes_no_help_builder = ReplyKeyboardBuilder()
but_yes = KeyboardButton(text="Давай сыграем")
but_no = KeyboardButton(text="Не хочу играть")
but_help = KeyboardButton(text="/help")
yes_no_help_builder.row(but_yes, but_no, but_help)
yes_no_help = yes_no_help_builder.as_markup(resize_keyboard=True)

rock_paper_scissors_btn = ReplyKeyboardBuilder()
rock = KeyboardButton(text="🗿")
paper = KeyboardButton(text="📜")
scissors = KeyboardButton(text="✂️")
rock_paper_scissors_btn.add(rock, paper, scissors)
