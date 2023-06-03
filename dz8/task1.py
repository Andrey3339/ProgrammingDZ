# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot

bot = telebot.TeleBot("6009215420:AAFVZBKDweF8vt31otEPAL4paEpEBmuy5e8")


@bot.message_handler(commands=['start']) 
def send_welcome(message):
	bot.send_message(message.from_user.id, "Привет, я бот Питоша, задавайте свои вопросы и скоро получите мои ответы.")
	
@bot.message_handler(content_types=['text'])
def text_message(message):
	data = open(file="question.txt", mode="a+", encoding="utf-8")
	text = f'{message.from_user.id}:{message.from_user.first_name} {message.from_user.last_name}:{message.text}\n'
	data.write(text)
	data.close()

        

bot.polling()