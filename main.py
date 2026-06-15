import asyncio
from aiogram import Bot, Dispatcher
from config import 8840128817:AAHXz5o4v_HrwW9UJfa3Ne7C1Vnd1cwowc8
import handlers

bot = Bot(8840128817:AAHXz5o4v_HrwW9UJfa3Ne7C1Vnd1cwowc8)
dp = Dispatcher()

dp.include_router(handlers.router)

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
