import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Я простой тестовый бот.",
    )

def main() -> None:
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        logging.error("Telegram Bot Token не найден в переменных окружения!")
        return

    # Исправленная инициализация:
    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))

    logging.info("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()