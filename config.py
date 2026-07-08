import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
EXTERNAL_RECOMMENDATIONS_URL = os.getenv("EXTERNAL_RECOMMENDATIONS_URL")
AI_API_URL = os.getenv("AI_API_URL", "http://127.0.0.1:8000")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("Не задан TELEGRAM_BOT_TOKEN в .env")
