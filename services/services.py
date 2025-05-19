import random

from lexicon.lexicon import LEXICON_GAME


def get_bot_choice():
    return random.choice(["rock", "paper", "scissors"])


def user_answer(item):
    for key in LEXICON_GAME:
        if LEXICON_GAME[key] == item:
            break
    return key


def get_winner(user_choice, bot_choice, lexicon):
    user_choice = user_answer(user_choice)
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if user_choice == bot_choice:
        return lexicon["nobody_won"]
    elif rules[user_choice] == bot_choice:
        return lexicon["user_won"]
    return lexicon["bot_won"]
