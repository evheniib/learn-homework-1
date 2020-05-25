"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem +
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars +
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split()) +
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета. +

"""
import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    print ("Вызван /start")
    update.message.reply_text("Hello, is you my creator?")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet_info (update, context):
    dt_now = datetime.now()
    dt_now = dt_now.strftime('%Y/%m/%d')
    user_text = update.message.text.split()
    planet_dict = {
        "Mercury": ephem.Mercury(dt_now), 
        "Venus": ephem.Venus(dt_now), 
        "Mars": ephem.Mars(dt_now), 
        "Jupiter": ephem.Jupiter(dt_now), 
        "Saturn": ephem.Saturn(dt_now), 
        "Uranus": ephem.Uranus(dt_now), 
        "Neptune": ephem.Neptune(dt_now)
    }
    if len(user_text) == 2:
        word = user_text[1].capitalize()
        print(word)
        if word in planet_dict:
            constellation = ephem.constellation(planet_dict[word])
            update.message.reply_text(constellation) 
        elif word == "Earth":
            update.message.reply_text("Earth has no constellation")
        else:
            update.message.reply_text("Wrong planet pls enter correct name of planet")
    else:
        update.message.reply_text("Wrong command. Pls type for example '/planet Mars'")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")

    mybot.start_polling()

    mybot.idle()

if __name__ == "__main__":
    main()