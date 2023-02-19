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


def planet_info(update, context):
    text = update.message.text.split(" ")[1]
    constellation = ephem.constellation(all_planet[text.capitalize()])

    if text.capitalize() in all_planet:
        update.message.reply_text(constellation)
    else:
        update.message.reply_text("Не наблюдается")


def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)


def wordcount(update, context):
    word_count = update.message.text.split(" ")[1:]
    update.message.reply_text(f"количество слов {len(word_count)}")


def moon(update, context):
    moon = ephem.next_full_moon(datetime.date.today())
    moon_date = update.message.text.split(" ")[1]
    if moon_date.capitalize() == "Затмение":
        update.message.reply_text(moon)
    else:
        update.message.reply_text("Когда же?")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("moon", moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
