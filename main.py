import asyncio # для асинхронного запуска бота
import logging # для настройки логгирования, которое поможет в отладке

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode # aiogram.enums.parse_mode - содержит настройки разметки 
# сообщений (HTML, markdown)
from aiogram.fsm.storage.memory import MemoryStorage # хранилища данных для состояний пользователей

import config # настройки бота, пока что только токен
from handlers import router # пока пустой, но скоро мы напишем в нём функционал нашего бота
from config_reader import config


async def main():
    # Для записей с типом Secret* необходимо 
    # вызывать метод get_secret_value(), 
    # чтобы получить настоящее содержимое вместо '*******'
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage()) # говорит о том, что все данные бота, 
    # которые мы не сохраняем в БД (к примеру состояния), будут стёрты при перезапуске.
    # Этот вариант является оптимальным, так как хранение состояний диспетчера требуется редко.
    dp.include_router(router) #  подключает к нашему диспетчеру все обработчики,
    # которые используют router
    await bot.delete_webhook(drop_pending_updates=True) # удаляет все обновления,
    # которые произошли после последнего завершения работы бота. 
    # Это нужно, чтобы бот обрабатывал только те сообщения, которые пришли ему
    # непосредственно во время его работы, а не за всё время
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) # запуск бота


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
