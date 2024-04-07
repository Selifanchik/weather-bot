import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from apps.bot import BotConversation
from apps.constants import TOKEN
from apps.constants_access import DIALECT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, HOST

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()



if __name__ == '__main__':

    logger.info(f'######{TOKEN}')

    application = ApplicationBuilder().token(TOKEN).build()
    stages = BotConversation()
    app_handler = stages.metcast()
    
    application.add_handler(app_handler)

    application.run_polling()