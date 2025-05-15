import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import Config, load_config
from handlers import user_handlers, other_handlers

async def main():
    # Включаем логирование
    logging.basicConfig(level=logging.INFO)
    
    config: Config = load_config()
    print(config.tg_bot.token)
    # Инициализируем бота и диспетчер
    bot = Bot(token=config.tg_bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    # Подключаем роутер с хендлерами
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    
    # Удаляем все обновления, которые произошли после последнего выключения бота
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())