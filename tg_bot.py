import logging
import ephem, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

all_planet = {
    "Марс": ephem.Mars(datetime.date.today()), "Венера": ephem.Venus(datetime.date.today()),
    "Меркурий": ephem.Mercury(datetime.date.today()),
    "Юпитер": ephem.Jupiter(datetime.date.today()), "Нептун": ephem.Neptune(datetime.date.today()),
    "Сатурн": ephem.Saturn(datetime.date.today()), "Уран": ephem.Uranus(datetime.date.today())
}


def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Hello user, спроси про 'Планеты'")


def talk_to_me(update, context):
    text = update.message.text
    constellation = ephem.constellation(all_planet[text.capitalize()])
    if text in all_planet:
        print(update.message.reply_text(constellation))
    else:
        print(text)
        update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
