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
    'ACCEPTED_GLASS': "{}Что принимается".format(emojize(':glass_of_milk:')),
    'REJECTED_GLASS': "{}Что не принимается".format(emojize(':glass_of_milk:')),
    'PREPARATION_GLASS': "{}Как подготовить к сдаче".format(emojize(':glass_of_milk:')),
    'MEANING_GLASS': "{}Зачем сдавать".format(emojize(':glass_of_milk:')),
    'LOCATION_GLASS': "{}Куда сдавать".format(emojize(':glass_of_milk:')),
    'ACCEPTED_PAPER': "{}Что принимается".format(emojize(':newspaper:')),
    'REJECTED_PAPER': "{}Что не принимается".format(emojize(':newspaper:')),
    'PREPARATION_PAPER': "{}Как подготовить к сдаче".format(emojize(':newspaper:')),
    'MEANING_PAPER': "{}Зачем сдавать".format(emojize(':newspaper:')),
    'LOCATION_PAPER': "{}Куда сдавать".format(emojize(':newspaper:')),
    'ACCEPTED_PLASTIC': "{}Что принимается".format(emojize(':lotion_bottle:')),
    'REJECTED_PLASTIC': "{}Что не принимается".format(emojize(':lotion_bottle:')),
    'PREPARATION_PLASTIC': "{}Как подготовить к сдаче".format(emojize(':lotion_bottle:')),
    'MEANING_PLASTIC': "{}Зачем сдавать".format(emojize(':lotion_bottle:')),
    'LOCATION_PLASTIC': "{}Куда сдавать".format(emojize(':lotion_bottle:')),
    'ACCEPTED_METAL': "{}Что принимается".format(emojize(':canned_food:')),
    'REJECTED_METAL': "{}Что не принимается".format(emojize(':canned_food:')),
    'PREPARATION_METAL': "{}Как подготовить к сдаче".format(emojize(':canned_food:')),
    'MEANING_METAL': "{}Зачем сдавать".format(emojize(':canned_food:')),
    'LOCATION_METAL': "{}Куда сдавать".format(emojize(':canned_food:')),
    'ACCEPTED_BATTERY': "{}Что принимается".format(emojize(':battery:')),
    'PREPARATION_BATTERY': "{}Как подготовить к сдаче".format(emojize(':battery:')),
    'MEANING_BATTERY': "{}Зачем сдавать".format(emojize(':battery:')),
    'LOCATION_BATTERY': "{}Куда сдавать".format(emojize(':battery:')),
    'ACCEPTED_TETRAPAK': "{}Что принимается".format(emojize(':beverage_box:')),
    'PREPARATION_TETRAPAK': "{}Как подготовить к сдаче".format(emojize(':beverage_box:')),
    'MEANING_TETRAPAK': "{}Зачем сдавать".format(emojize(':beverage_box:')),
    'LOCATION_TETRAPAK': "{}Куда сдавать".format(emojize(':beverage_box:')),
    'ACCEPTED_BULB': "{}Что принимается".format(emojize(':light_bulb:')),
    'PREPARATION_BULB': "{}Как подготовить к сдаче".format(emojize(':light_bulb:')),
    'MEANING_BULB': "{}Зачем сдавать".format(emojize(':light_bulb:')),
    'LOCATION_BULB': "{}Куда сдавать".format(emojize(':light_bulb:')),
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help"
}
