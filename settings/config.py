# импортируем модуль emoji для отображения эмоджи
from emoji import emojize
# импортируем os для доступа к переменным среды окружения
import os
# импортируем библиотеку dotenv для удобного доступа к скрытым ключам
import dotenv
dotenv.load_dotenv('.env')
# токен Telegram бота
BOT_TOKEN = os.environ['BOT_TOKEN']
# токен 2ГИС
MAP_TOKEN = os.environ['MAP_TOKEN']
# версия приложения
VERSION = '1.0.0'
# автор приложения
AUTHOR = 'Mikhail Galdin'

# кнопки управления
KEYBOARD = {
    'GLASS': emojize(':glass_of_milk: Стекло'),
    'PAPER': emojize(':newspaper: Бумага'),
    'PLASTIC': emojize(':lotion_bottle: Пластик'),
    'METAL': emojize(':canned_food: Металл'),
    'TETRAPAK': emojize(':beverage_box: Тетрапак'),
    'BATTERY': emojize(':battery: Батарейки'),
    'BULB': emojize(':light_bulb: Лампочки'),
    'ABOUT_US': emojize(':information: О продукте'),
    'BACK_TO_MENU': emojize('⏪ Назад'),
    'ACCEPTED_GLASS': "Что принимается",
    'REJECTED_GLASS': "Что не принимается",
    'PREPARATION_GLASS': "Как подготовить к сдаче",
    'MEANING_GLASS': "Зачем сдавать",
    'LOCATION_GLASS': "Куда сдавать",
    'ACCEPTED_PAPER': "Что принимается",
    'REJECTED_PAPER': "Что не принимается",
    'PREPARATION_PAPER': "Как подготовить к сдаче",
    'MEANING_PAPER': "Зачем сдавать",
    'LOCATION_PAPER': "Куда сдавать",
    'ACCEPTED_PLASTIC': "Что принимается",
    'REJECTED_PLASTIC': "Что не принимается",
    'PREPARATION_PLASTIC': "Как подготовить к сдаче",
    'MEANING_PLASTIC': "Зачем сдавать",
    'LOCATION_PLASTIC': "Куда сдавать",
    'ACCEPTED_METAL': "Что принимается",
    'REJECTED_METAL': "Что не принимается",
    'PREPARATION_METAL': "Как подготовить к сдаче",
    'MEANING_METAL': "Зачем сдавать",
    'LOCATION_METAL': "Куда сдавать",
    'ACCEPTED_BATTERY': "Что принимается",
    'PREPARATION_BATTERY': "Как подготовить к сдаче",
    'MEANING_BATTERY': "Зачем сдавать",
    'LOCATION_BATTERY': "Куда сдавать",
    'ACCEPTED_TETRAPAK': "Что принимается",
    'PREPARATION_TETRAPAK': "Как подготовить к сдаче",
    'MEANING_TETRAPAK': "Зачем сдавать",
    'LOCATION_TETRAPAK': "Куда сдавать",
    'ACCEPTED_BULB': "Что принимается",
    'PREPARATION_BULB': "Как подготовить к сдаче",
    'MEANING_BULB': "Зачем сдавать",
    'LOCATION_BULB': "Куда сдавать",
}

# названия команд
COMMANDS = {
    'START': "start",
}
