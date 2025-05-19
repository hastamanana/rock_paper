from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="/help", description="тест команды help"),
        BotCommand(command="/contacts",
                   description="контакты админа бота: @wolk"),
        BotCommand(command="/payments", description="Платежи"),
    ]

    await bot.set_my_commands(main_menu_commands)
