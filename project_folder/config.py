import os
from dotenv import load_dotenv

load_dotenv()
#извлекаем из .env Токен Бота
TOKEN = str(os.getenv("BOT_TOKEN"))