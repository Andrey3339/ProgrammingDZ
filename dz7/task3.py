# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.
# Описание ботов https://pypi.org/project/pyTelegramBotAPI/

import telebot
import requests
import time


bot = telebot.TeleBot("6009215420:AAFVZBKDweF8vt31otEPAL4paEpEBmuy5e8")

@bot.message_handler(commands=['start', 'help']) # - это декоратор, бот реагирует на команды /start и /help
# мы создаем функцию send_welcome()
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

# глобальные переменные для игры 
is_game = False
rand_int = 0
count = 0

# бот реагирует на текст
@bot.message_handler(content_types=['text'])
def greetings(message):
  
    #print(message) # message - это объект в формате json (ключ - значение, в качестве значения могут быть другие словари)
    text = message.text
    text = text.lower()
    global is_game, rand_int, count
    
    if 'привет' in text: # если во входящем тексте от пользователя есть слово привет - бот поздаровается
        bot.reply_to(message, f'Приветствую тебя, {message.from_user.first_name}')

    # добавляем модуль для определения погоды с помощью сайта wttr.in

    elif text == 'погода':  
         req = requests.get('https://wttr.in/?0T')
         bot.reply_to(message, req.text)

    # добавляем api с сайта котики

    elif text == 'котики':
         req = requests.get(f'https://cataas.com/cat?{time.time()}')
         bot.send_photo(message.chat.id, req.content) # пересылаем в id чата (message.message_id) фото котика по запросу

    elif is_game == True:
         val = int(text)
         count += 1
         if rand_int > val:
              bot.reply_to(message, "больше!")
         elif rand_int < val:
              bot.reply_to(message, "меньше!")
         elif rand_int == val:
              bot.reply_to(message, f"Ура, вы угадали число все за {count} попыток!")
              count = 0
              is_game = False
              rand_int = 0

    elif text == 'игра':
         from random import randint
         is_game = True
         rand_int = randint(1, 1001)
         bot.reply_to(message, "Я загадал число от 1 до 1000, попробуй его отгадать - введите число: ")
    
     

bot.polling() # - здесь бот начинает просматривать список событий, это как бы осел из Шрека - приехали? а щас? ....




