import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши сообщение в поддержку')


@bot.message_handler(content_types=["text"])
def messages(message):
    if int(message.chat.id) == int(config.owner):
        try:
            bot.send_message(message.reply_to_message.text.split(':')[0], message.text)
            # print(f"id from - {(message.reply_to_message.text).split(':')[0]} id who - {message.chat.id} text - {
            # message.text}")
        except:
            bot.send_message(message.chat.id, "Сделайте ответ на сообщение")
    else:
        bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
        bot.send_message(message.chat.id, f'Ожидайте ответа')
        print(message)

try:
    bot.polling(none_stop=True)
except:
    pass