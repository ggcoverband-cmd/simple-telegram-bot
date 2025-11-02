import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования (помогает отслеживать ошибки)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция-обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Я простой тестовый бот.",
    )

def main() -> None:
    # Получаем токен бота из переменной окружения
    # Это самый безопасный способ хранить токен!
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        logging.error("Telegram Bot Token не найден в переменных окружения!")
        return

    # Создаем экземпляр ApplicationBuilder
    # Он отвечает за управление ботом
    application = ApplicationBuilder().token(bot_token).build()

    # Добавляем обработчик команды /start
    # Когда пользователь отправит /start, будет вызвана функция start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    logging.info("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()