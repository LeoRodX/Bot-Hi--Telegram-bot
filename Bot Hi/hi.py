import telebot
from secrets import secrets
from telebot import types

token = secrets.get('BOT_API_TOKEN')  # Получение токена, который лучше хранить в справочнике файла secrets.py
bot = telebot.TeleBot(token) # Создадим соединение с ботом

# Обработчик сообщений польователя бота
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Отправка ответа пользователю, на ввод им любого текста.
    bot.send_message(message.from_user.id, "Ну, здравствуй, мир!")

# бесконечное выполнение кода
while True:
    try:
      bot.polling(none_stop=True, interval=0)
    except:
      continue

