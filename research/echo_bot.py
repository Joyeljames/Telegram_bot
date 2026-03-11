import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()
telegram_bot_token = os.getenv("Telebot_key")

# print(telegram_bot_token)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends a message with the command /start or /help.
    """

    await message.reply("Hi! I'm an brainy Bot. powered by joyel. I can echo your messages back to you. Just send me anything!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)