from pathlib import Path

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters


CITY = 0


class BotConversation:
    def metcast(self):
        return ConversationHandler(
            entry_points=[CommandHandler('start', BotConversation.start)],
            states={
                CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, BotConversation.get_city)]
                },
            fallbacks=[CommandHandler('cancel', BotConversation.cancel)]
        )


    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data.clear()
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Хотите узнать погоду?")
        await update.message.reply_text('Какой город Вас интересует')
        return CITY



    @staticmethod
    async def cancel(update:Update):
        user = update.message.from_user
        await update.message.reply_text(
            f'Bye {user}!', reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    

    @staticmethod
    async def get_city(update:Update, context: ContextTypes.DEFAULT_TYPE):
        user_data = context.user_data
        text = update.message.text
        user_data = text
        await update.message.reply_text(f'Минутку, проверяем данные, Выввели город {text}')
        return ConversationHandler.END
    