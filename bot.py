import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TELEGRAM_BOT_TOKEN, AI_API_URL

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Напиши /recommend, чтобы получить рекомендации товаров."
    )

@dp.message(Command("recommend"))
async def cmd_recommend(message: types.Message):
    user_text = "default"
    try:
        r = requests.post(
            f"{AI_API_URL}/recommendations",
            json={"category": user_text},
            timeout=5,
        )
        r.raise_for_status()
        items = r.json()
        if not items:
            await message.answer("Пока нет рекомендаций.")
            return

        text = "Рекомендации:\n\n"
        for i, item in enumerate(items, 1):
            text += f"{i}. {item['title']}\n{item['body'][:100]}...\n\n"
        await message.answer(text)
    except Exception as e:
        await message.answer(f"Что-то пошло не так: {e}")

async def main():
    print("Бот запущен и готов к работе!")
    print("Ожидание команд от пользователей...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())