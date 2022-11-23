import telebot
import requests
from bs4 import BeautifulSoup as b

URL = 'https://kaktus.media/?lable=8&date=2022-11-23&order=time'
API_KEY = '5713840834:AAE2neVZIBriZAtNANQ5SsVfBZNMFNV5VJk'



keybord = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# кнопки
button = telebot.types.KeyboardButton('Quit')

# обеденение
keybord.add(button)


    


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    tel = soup.find_all('div', class_='ArticleItem')
    return [c.text for c in tel]



list_of_jokes = parser(URL)
# print(list_of_jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Quit'])
def check(message):
    for message in message:
        bot.send_message(message.chat.id, 'До свидания')
        break
        

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'HELLO: ')



@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']:
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите только цифру: ')


bot.polling()