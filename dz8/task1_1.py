# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.

import telebot

bot = telebot.TeleBot("6009215420:AAFVZBKDweF8vt31otEPAL4paEpEBmuy5e8")

with open(file="question.txt", mode="r", encoding="utf-8") as data:
    questions = data.readlines()

for quest in questions:
    list_quest = quest.split(':')
    answer = input("Введите ответ на вопрос - " + list_quest[2])
    bot.send_message(list_quest[0], f"Привет, {list_quest[1]}, вы спрашивали {list_quest[2]}")
    bot.send_message(list_quest[0], f"Наш ответ:  {answer}")







