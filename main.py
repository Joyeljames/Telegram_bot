from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load environment variables
load_dotenv()
telegram_bot_token = os.getenv("Telebot_key")

# Load DialoGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None


# Initialize Telegram bot
bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)


def clear():
    """
    Clear conversation memory
    """
    global chat_history_ids
    chat_history_ids = None


# /clear command
@dp.message_handler(commands=['clear'])
async def clear_reference(message: types.Message):
    clear()
    await message.reply("I have cleared the past conversation!")


# /start command
@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.reply(
        "Hi! I'm a Brainy AI Bot powered by Joyel 🤖\n"
        "Send me any message and I will reply!"
    )


# /help command
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):

    help_text = """
Hi there! I'm a Telegram AI chatbot created by Joyel.

Available commands:

/start - Start the bot
/help - Show help message
/clear - Clear conversation history

Just send me any message and I will reply using AI!
"""

    await message.reply(help_text)


# Main chatbot handler
@dp.message_handler()
async def handle_message(message: types.Message):

    global chat_history_ids

    user_input = message.text

    print(f">>> User: {user_input}")

    # Encode user message
    new_user_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token,
        return_tensors='pt'
    )

    # Append conversation history
    bot_input_ids = (
        torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
        if chat_history_ids is not None
        else new_user_input_ids
    )

    # Generate bot response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95
    
    )

    # Decode response
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print(f">>> Bot: {response}")

    await message.reply(response)


# Run bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)