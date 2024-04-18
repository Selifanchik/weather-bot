from pathlib import Path

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
from apps.constants import WEATHER_TOKEN
from apps.weatherapi import Requests
from apps.weatherconst import WIND_DIR
# from apps.db.db import add_user, get_user

CITY = 0


class BotConversation:
    def metcast(self):
        return ConversationHandler(
            entry_points=[CommandHandler('start', BotConversation.start), MessageHandler(filters.TEXT & ~filters.COMMAND, BotConversation.get_city)],
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
    async def customweather(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Bla-bla')



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
        user_k = update.message.from_user
        # add_user(user_k.first_name, str(user_k.id), user_k.username)

        req = Requests(WEATHER_TOKEN) 
        
        data = req.getWeather(text) 
        
        if data.status_code == 200: 
            print(data.json())
            town = data.json()['location']['name']
            temp = data.json()['current']['temp_c']
            feelslike_temp = data.json()['current']['feelslike_c'] 
            condition = data.json()['current']['condition']['text']
            wind = data.json()['current']['wind_kph'] * 1000 / 3600
            wind_gust = data.json()['current']['gust_kph'] * 1000 / 3600
            wind_dir = WIND_DIR[data.json()['current']['wind_dir']]
            pressure_mb = data.json()['current']['pressure_mb'] / 1.333
            precip_mm = data.json()['current']['precip_mm']
            humidity = data.json()['current']['humidity']
            await update.message.reply_text(f'Погода в городе {town}:\n\
\n\
{condition} {temp} °C\n\
(ощущается как {feelslike_temp}°C)\n\
Ветер {wind_dir} {round(wind, 1)} м/c, порывы до {round(wind_gust, 1)} м/c\n\
Давление {round(pressure_mb, 1)} мм рт. ст.\n\
Осадки {precip_mm} мм\n\
Влажность {humidity}%')


        else:
            await update.message.reply_text(f'Проверьте правильность написания города {text} {data.status_code}')
        return ConversationHandler.END
    

    @staticmethod
    async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
        text_caps = ' '.join(context.args).upper()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)