# импортируем объекты клавиатур и кнопок клавиатур из Telegram Bot API
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
# импортируем созданную конфигурацию проекта
from settings import config
# импортируем словари сообщений от бота пользователю
from settings.message import GLASS_ACCEPTED_LIST, GLASS_ACCEPTED_PICTURES, GLASS_REJECTED_LIST, \
    GLASS_REJECTED_PICTURES, PAPER_ACCEPTED_LIST, PAPER_ACCEPTED_PICTURES, PAPER_REJECTED_LIST, PAPER_REJECTED_PICTURES, \
    PLASTIC_ACCEPTED_LIST, PLASTIC_ACCEPTED_PICTURES, PLASTIC_REJECTED_LIST, PLASTIC_REJECTED_PICTURES, \
    METAL_ACCEPTED_LIST, METAL_ACCEPTED_PICTURES, METAL_REJECTED_LIST, METAL_REJECTED_PICTURES, BATTERY_ACCEPTED_LIST, \
    BATTERY_ACCEPTED_PICTURES


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """

    # инициализация разметки
    def __init__(self):
        self.markup = None

    def set_btn(self, name):
        """
        Метод создает и возвращает кнопку по входным параметрам
        :param name: Имя кнопки
        :return: Сконфигурированная кнопка типа KeyboardButton
        """
        # Для кнопок с отправкой геолокации необходимо указать это свойство
        if name.find("LOCATION") != -1:
            return KeyboardButton(config.KEYBOARD[name], request_location=True)
        # Для стандартных кнопок с отправкой сообщений
        return KeyboardButton(config.KEYBOARD[name])

    def set_inline_btn(self, item, category):
        """
        Метод создает и возвращает inline-кнопку по входным параметрам
        :param item: Индекс кнопки
        :param category: Словарь категории отходов
        :return: Сконфигурированная кнопка типа InlineKeyboardButton
        """
        return InlineKeyboardButton(category[item],
                                    url=self.choose_url(item, category))

    def set_inline_menu(self, category):
        """
        Метод создает разметку inline-кнопок в выбранной категории отходов и возвращает её
        :param category: Словарь категории отходов
        :return: Сконфигурированная клавиатура типа InlineKeyboardMarkup
        """
        self.markup = InlineKeyboardMarkup()
        # Перебираем весь словарь и создаём соответствующие кнопки
        for item in category:
            self.markup.add(self.set_inline_btn(item, category))
        return self.markup

    def choose_url(self, item, category):
        """
        Метод по заданной категории отходов и индексу возвращает ссылку
        на пост во вспомогательном Telegram-канале
        :param item: Индекс кнопки
        :param category: Словарь категории отходов
        :return: URL необходимого поста вспомогательного Telegram-канала
        """
        if category == GLASS_ACCEPTED_LIST:
            return GLASS_ACCEPTED_PICTURES[item]
        elif category == GLASS_REJECTED_LIST:
            return GLASS_REJECTED_PICTURES[item]
        elif category == PAPER_ACCEPTED_LIST:
            return PAPER_ACCEPTED_PICTURES[item]
        elif category == PAPER_REJECTED_LIST:
            return PAPER_REJECTED_PICTURES[item]
        elif category == PLASTIC_ACCEPTED_LIST:
            return PLASTIC_ACCEPTED_PICTURES[item]
        elif category == PLASTIC_REJECTED_LIST:
            return PLASTIC_REJECTED_PICTURES[item]
        elif category == METAL_ACCEPTED_LIST:
            return METAL_ACCEPTED_PICTURES[item]
        elif category == METAL_REJECTED_LIST:
            return METAL_REJECTED_PICTURES[item]
        elif category == BATTERY_ACCEPTED_LIST:
            return BATTERY_ACCEPTED_PICTURES[item]

    def main_menu(self):
        """
        Метод создает разметку кнопок в главном меню и возвращает её
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        # Конфигурация 1 ряда кнопок
        glass_button = self.set_btn('GLASS')
        paper_button = self.set_btn('PAPER')
        self.markup.row(glass_button, paper_button)

        # Конфигурация 2 ряда кнопок
        plastic_button = self.set_btn('PLASTIC')
        metal_button = self.set_btn('METAL')
        self.markup.row(plastic_button, metal_button)

        # Конфигурация 3 ряда кнопок
        battery_button = self.set_btn('BATTERY')
        tetrapak_button = self.set_btn('TETRAPAK')
        self.markup.row(battery_button, tetrapak_button)

        # Конфигурация 4 ряда кнопок
        bulb_button = self.set_btn('BULB')
        about_us_button = self.set_btn('ABOUT_US')
        self.markup.row(bulb_button, about_us_button)
        return self.markup

    def about_us_menu(self):
        """
        Метод создает разметку кнопок в меню about_us и settings
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        back_to_menu_button = self.set_btn('BACK_TO_MENU')
        self.markup.row(back_to_menu_button)
        return self.markup

    def glass_menu(self):
        """
        Метод создает разметку кнопок в меню отходов "Стекло"
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        accepted_button = self.set_btn('ACCEPTED_GLASS')
        rejected_button = self.set_btn('REJECTED_GLASS')
        preparation_button = self.set_btn('PREPARATION_GLASS')
        meaning_button = self.set_btn('MEANING_GLASS')
        location_button = self.set_btn('LOCATION_GLASS')
        back_button = self.set_btn('BACK_TO_MENU')
        self.markup.add(accepted_button, rejected_button, preparation_button,
                        meaning_button, location_button, back_button)
        return self.markup

    def paper_menu(self):
        """
        Метод создает разметку кнопок в меню отходов "Бумага"
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        accepted_button = self.set_btn('ACCEPTED_PAPER')
        rejected_button = self.set_btn('REJECTED_PAPER')
        preparation_button = self.set_btn('PREPARATION_PAPER')
        meaning_button = self.set_btn('MEANING_PAPER')
        location_button = self.set_btn('LOCATION_PAPER')
        back_button = self.set_btn('BACK_TO_MENU')
        self.markup.add(accepted_button, rejected_button, preparation_button,
                        meaning_button, location_button, back_button)
        return self.markup

    def plastic_menu(self):
        """
        Метод создает разметку кнопок в меню отходов "Пластик"
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        accepted_button = self.set_btn('ACCEPTED_PLASTIC')
        rejected_button = self.set_btn('REJECTED_PLASTIC')
        preparation_button = self.set_btn('PREPARATION_PLASTIC')
        meaning_button = self.set_btn('MEANING_PLASTIC')
        location_button = self.set_btn('LOCATION_PLASTIC')
        back_button = self.set_btn('BACK_TO_MENU')
        self.markup.add(accepted_button, rejected_button, preparation_button,
                        meaning_button, location_button, back_button)
        return self.markup

    def metal_menu(self):
        """
        Метод создает разметку кнопок в меню отходов "Металл"
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        accepted_button = self.set_btn('ACCEPTED_METAL')
        rejected_button = self.set_btn('REJECTED_METAL')
        preparation_button = self.set_btn('PREPARATION_METAL')
        meaning_button = self.set_btn('MEANING_METAL')
        location_button = self.set_btn('LOCATION_METAL')
        back_button = self.set_btn('BACK_TO_MENU')
        self.markup.add(accepted_button, rejected_button, preparation_button,
                        meaning_button, location_button, back_button)
        return self.markup

    def battery_menu(self):
        """
        Метод создает разметку кнопок в меню отходов "Батарейки"
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        accepted_button = self.set_btn('ACCEPTED_BATTERY')
        preparation_button = self.set_btn('PREPARATION_BATTERY')
        meaning_button = self.set_btn('MEANING_BATTERY')
        location_button = self.set_btn('LOCATION_BATTERY')
        back_button = self.set_btn('BACK_TO_MENU')
        self.markup.add(accepted_button, preparation_button,
                        meaning_button, location_button, back_button)
        return self.markup

    def tetrapak_menu(self):
        """
        Метод создает разметку кнопок в меню отходов "Тетрапак"
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        accepted_button = self.set_btn('ACCEPTED_TETRAPAK')
        preparation_button = self.set_btn('PREPARATION_TETRAPAK')
        meaning_button = self.set_btn('MEANING_TETRAPAK')
        location_button = self.set_btn('LOCATION_TETRAPAK')
        back_button = self.set_btn('BACK_TO_MENU')
        self.markup.add(accepted_button, preparation_button,
                        meaning_button, location_button, back_button)
        return self.markup

    def bulb_menu(self):
        """
        Метод создает разметку кнопок в меню отходов "Лампочки"
        :return: Сконфигурированная клавиатура типа ReplyKeyboardMarkup
        """
        self.markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        accepted_button = self.set_btn('ACCEPTED_BULB')
        preparation_button = self.set_btn('PREPARATION_BULB')
        meaning_button = self.set_btn('MEANING_BULB')
        location_button = self.set_btn('LOCATION_BULB')
        back_button = self.set_btn('BACK_TO_MENU')
        self.markup.add(accepted_button, preparation_button,
                        meaning_button, location_button, back_button)
        return self.markup
