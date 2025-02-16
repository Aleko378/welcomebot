from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '7707993674:AAFtcJyp9qjUFeazLejeLxk26gpdJ489dzA'

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    await update.message.reply_text(
        f'Здравствуйте, {user.first_name}! Я — Александр, специалист по созданию чат-ботов.\n'
        'Я разрабатываю чат-ботов для Telegram, WhatsApp и VK, помогая автоматизировать процессы и улучшать бизнес.\n'
        'Команды:\n/about — О моей работе\n/contact — Мои контакты\n/help — Список команд'
    )

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Список команд:\n/start — Приветствие\n/about — О моей работе\n/contact — Мои контакты')

async def about_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Я создаю чат-ботов под ключ для Telegram, WhatsApp и VK.\n'
        'Услуги: автоматизация заказов, поддержка клиентов, интеграция с CRM и многое другое.\n'
        'Каждый проект — индивидуальный подход и высокое качество.'
    )

async def contact_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Мои контакты:\nTelegram: @aleko_b\nWhatsApp: +79992105007\nEmail: aleko378@gmail.com'
    )

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text('Спасибо за сообщение! Напишите /about или /contact для деталей.')

async def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("contact", contact_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logging.info("Бот запущен.")

    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    try:
        await asyncio.Event().wait()
    finally:
        await application.stop()
        await application.shutdown()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())