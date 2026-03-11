# Telegram AI Chatbot 🤖

This project is a Telegram chatbot built using Python and Hugging Face Transformers.
The bot uses the DialoGPT conversational AI model to generate responses and interact with users in real time.

## 🚀 Features

* Telegram chatbot integration
* AI-powered responses using DialoGPT
* Conversation memory
* Commands for controlling the bot
* Secure environment variable handling

## 🧠 Technologies Used

* Python
* Aiogram (Telegram bot framework)
* Hugging Face Transformers
* DialoGPT conversational model
* python-dotenv

## 📂 Project Structure

telegram-ai-chatbot/

├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env (not uploaded to GitHub)

## ⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/telegram-ai-chatbot.git

Navigate to the project folder:

cd telegram-ai-chatbot

Install dependencies:

pip install -r requirements.txt

## 🔑 Setup Environment Variables

Create a `.env` file and add your Telegram bot token:

Telebot_key=YOUR_TELEGRAM_BOT_TOKEN

You can get a bot token from Telegram BotFather.

## ▶️ Running the Bot

Run the bot using:

python main.py

The bot will start listening for messages on Telegram.

## 💬 Bot Commands

/start — Start the bot
/help — Show help message
/clear — Clear conversation history

## 📌 Example Interaction

User: Hello
Bot: Hi! How can I help you today?

User: What is AI?
Bot: Artificial Intelligence is a field of computer science that enables machines to perform tasks that normally require human intelligence.

## 📈 Future Improvements

* Add vector database for long-term memory
* Add document question answering (RAG)
* Deploy the bot to cloud for 24/7 usage
* Build a web interface

## 👨‍💻 Author

Joyel James
