import telebot
import wikipedia
import config


bot = telebot.TeleBot(config.token)  # создание бота
wikipedia.set_lang("ru")  # язык в Wiki


@bot.message_handler(commands=["start"])  # /start
def start(message):
    bot.send_message(message.chat.id, 'Отправь мне любое слово, и я найду его значение на Wikipedia')

@bot.message_handler(commands=["help"])  # /help
def helps(message):
    bot.send_message(message.chat.id, 'Я любознательный Бот и черпаю свои знания на Wikipedia :-) '
                                  'Отправь мне любое слово, и я найду его значение на Wikipedia')


@bot.message_handler(content_types=["text"])
def find_text(message):
    find_text = message.text

    try:
        wiki_txt = wikipedia.summary(find_text, sentences=3)
        wiki_photo = wikipedia.page(find_text).images[1]

    except BaseException:  # исключения
        wiki_txt = 'В энциклопедии нет информации об этом'
        wiki_photo = 'Фото нет('
    bot.send_message(message.chat.id, wiki_txt)
    bot.send_photo(message.chat.id, photo=wiki_photo)


bot.polling(none_stop=True, interval=0)
