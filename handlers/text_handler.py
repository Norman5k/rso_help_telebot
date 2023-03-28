# импортируем math для округления числа
import math
# импортируем Path для получения пути до файла-изображения
from pathlib import Path
# импортируем requests для отправки GET-запросов к 2Gis API
import requests
# импортируем абстрактный обработчик
from handlers.abstract_handler import Handler
# импортируем созданную конфигурацию проекта
from settings import config
# импортируем словари сообщений от бота пользователю
from settings.message import MESSAGES, GLASS_ACCEPTED_LIST, GLASS_REJECTED_LIST, PAPER_ACCEPTED_LIST, \
    PAPER_REJECTED_LIST, PLASTIC_ACCEPTED_LIST, PLASTIC_REJECTED_LIST, METAL_ACCEPTED_LIST, METAL_REJECTED_LIST, \
    BATTERY_ACCEPTED_LIST


class TextHandler(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)
        self.category = 'menu'

    def pressed_btn_about_us(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия на кнопку "О продукте"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['info_about'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.about_us_menu())

    def pressed_btn_back(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия на кнопку "Назад"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['info_when_back'],
                              reply_markup=self.keyboards.main_menu())

    def pressed_btn_glass(self, message):
        """
        Метод обрабатываем входящие текстовые сообщения от нажатий на кнопку "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_category'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.glass_menu())

    def pressed_btn_paper(self, message):
        """
        Метод обрабатываем входящие текстовые сообщения от нажатий на кнопку "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_category'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.paper_menu())

    def pressed_btn_plastic(self, message):
        """
        Метод обрабатываем входящие текстовые сообщения от нажатий на кнопку "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_category'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.plastic_menu())

    def pressed_btn_metal(self, message):
        """
        Метод обрабатываем входящие текстовые сообщения от нажатий на кнопку "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_category'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.metal_menu())

    def pressed_btn_bulb(self, message):
        """
        Метод обрабатываем входящие текстовые сообщения от нажатий на кнопку "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_category'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.bulb_menu())

    def pressed_btn_tetrapak(self, message):
        """
        Метод обрабатываем входящие текстовые сообщения от нажатий на кнопку "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_category'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.tetrapak_menu())
    def pressed_btn_battery(self, message):
        """
        Метод обрабатываем входящие текстовые сообщения от нажатий на кнопку "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_category'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.battery_menu())

    # _____________________________Обработка кнопок в категории "Cтекло"______________________________

    def pressed_btn_accepted_glass(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что принимается" в категории "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['accepted_glass'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(GLASS_ACCEPTED_LIST))

    def pressed_btn_rejected_glass(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что не принимается" в категории "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['rejected_glass'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(GLASS_REJECTED_LIST))

    def pressed_btn_preparation_glass(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Как подготовить к сдаче" в категории "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['preparation_glass'],
                              parse_mode="HTML")

    def pressed_btn_meaning_glass(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Зачем сдавать" в категории "Стекло"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['meaning_glass'],
                              parse_mode="HTML")

    def pressed_btn_location_glass(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Куда сдавать" в категории "Стекло"
        :param message: Входящее сообщение
        """
        # Тег отходов категории "Стекло"
        tag = "reception_point_glass"
        self.search_nearest_point(message, tag)

    # ______________________________Обработка кнопок в категории "Бумага"______________________________

    def pressed_btn_accepted_paper(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что принимается" в категории "Бумага"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['accepted_paper'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(PAPER_ACCEPTED_LIST))

    def pressed_btn_rejected_paper(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что не принимается" в категории "Бумага"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['rejected_paper'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(PAPER_REJECTED_LIST))

    def pressed_btn_preparation_paper(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Как подготовить к сдаче" в категории "Бумага"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['preparation_paper'],
                              parse_mode="HTML")

    def pressed_btn_meaning_paper(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Зачем сдавать" в категории "Бумага"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['meaning_paper'],
                              parse_mode="HTML")

    def pressed_btn_location_paper(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Куда сдавать" в категории "Бумага"
        :param message: Входящее сообщение
        """
        # Тег отходов категории "Бумага"
        tag = "reception_point_paper"
        self.search_nearest_point(message, tag)

    # ______________________________Обработка кнопок в категории "Пластик"______________________________

    def pressed_btn_accepted_plastic(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что принимается" в категории "Пластик"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['accepted_plastic'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(PLASTIC_ACCEPTED_LIST))

    def pressed_btn_rejected_plastic(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что не принимается" в категории "Пластик"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['rejected_plastic'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(PLASTIC_REJECTED_LIST))

    def pressed_btn_preparation_plastic(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Как подготовить к сдаче" в категории "Пластик"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['preparation_plastic'],
                              parse_mode="HTML")

    def pressed_btn_meaning_plastic(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Зачем сдавать" в категории "Пластик"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['meaning_plastic'],
                              parse_mode="HTML")

    def pressed_btn_location_plastic(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Куда сдавать" в категории "Пластик"
        :param message: Входящее сообщение
        """
        # Тег отходов категории "Пластик"
        tag = "reception_point_pet_bottles"
        self.search_nearest_point(message, tag)

    # ______________________________Обработка кнопок в категории "Металл"______________________________

    def pressed_btn_accepted_metal(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что принимается" в категории "Металл"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['accepted_metal'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(METAL_ACCEPTED_LIST))

    def pressed_btn_rejected_metal(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что не принимается" в категории "Металл"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['rejected_metal'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(METAL_REJECTED_LIST))

    def pressed_btn_preparation_metal(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Как подготовить к сдаче" в категории "Металл"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['preparation_metal'],
                              parse_mode="HTML")

    def pressed_btn_meaning_metal(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Зачем сдавать" в категории "Металл"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['meaning_metal'],
                              parse_mode="HTML")

    def pressed_btn_location_metal(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Куда сдавать" в категории "Металл"
        :param message: Входящее сообщение
        """
        # Тег отходов категории "Металл"
        tag = "reception_point_aluminum_cans"
        self.search_nearest_point(message, tag)

    # ______________________________Обработка кнопок в категории "Лампочки"______________________________

    def pressed_btn_accepted_bulb(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что принимается" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        # запоминаем путь к файлу-изображению
        photo = open(Path("pictures", "bulb.png"), 'rb')
        self.bot.send_photo(message.chat.id,
                            photo=photo,
                            parse_mode="HTML",
                            caption=MESSAGES['accepted_bulb'])

    def pressed_btn_preparation_bulb(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Как подготовить к сдаче" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['preparation_bulb'],
                              parse_mode="HTML")

    def pressed_btn_meaning_bulb(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Зачем сдавать" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['meaning_bulb'],
                              parse_mode="HTML")

    def pressed_btn_location_bulb(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Куда сдавать" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        # Тег отходов категории "Лампочки"
        tag = "reception_point_container_bulbs"
        self.search_nearest_point(message, tag)

    # ______________________________Обработка кнопок в категории "Тетрапак"______________________________

    def pressed_btn_accepted_tetrapak(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что принимается" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        photo = open(Path("pictures", "tetrapak.png"), 'rb')
        self.bot.send_photo(message.chat.id,
                            photo=photo,
                            caption=MESSAGES['accepted_tetrapak'])

    def pressed_btn_preparation_tetrapak(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Как подготовить к сдаче" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['preparation_tetrapak'],
                              parse_mode="HTML")

    def pressed_btn_meaning_tetrapak(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Зачем сдавать" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['meaning_tetrapak'],
                              parse_mode="HTML")

    def pressed_btn_location_tetrapak(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Куда сдавать" в категории "Лампочки"
        :param message: Входящее сообщение
        """
        # Тег отходов категории "Тетрапак"
        tag = "reception_point_tetra_pac"
        self.search_nearest_point(message, tag)

    # ______________________________Обработка кнопок в категории "Батарейки"______________________________

    def pressed_btn_accepted_battery(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Что принимается" в категории "Батарейки"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['accepted_battery'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.set_inline_menu(BATTERY_ACCEPTED_LIST))

    def pressed_btn_preparation_battery(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Как подготовить к сдаче" в категории "Батарейки"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['preparation_battery'],
                              parse_mode="HTML")

    def pressed_btn_meaning_battery(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Зачем сдавать" в категории "Батарейки"
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['meaning_battery'],
                              parse_mode="HTML")

    def pressed_btn_location_battery(self, message):
        """
        Метод обрабатывает входящие текстовые сообщения от нажатия
        на кнопку "Куда сдавать" в категории "Батарейки"
        :param message: Входящее сообщение
        """
        # Тег отходов категории "Батарейки"
        tag = "reception_point_batteries"
        self.search_nearest_point(message, tag)

    def search_nearest_point(self, message, tag):
        """
        Метод ищет координаты ближайшей точки сбора выбранного вида отходов
        с помощью GET-запросов к 2ГИС Places API.
        Всего 2ГИС позволяет обработать 5 страниц запроса, то есть, 50 ближжайших точек.
        :param message: Входящее сообщение
        :param tag: Вид отходов
        """
        # Радиус поиска
        radius = 300
        # Тег ограничения доступности
        stop_tag = "additionalgarbage_availability_access_restricted"
        # Формирование строки запроса ближайших точек сбора отходов в радиусе 300 метров
        request_url = "https://catalog.api.2gis.com/3.0/items?q=раздельный сбор мусора и отходов&fields=items.point,filters&sort=distance&lon={}&lat={}&radius={}&work_time=now&key={}" \
            .format(message.location.longitude, message.location.latitude, radius, self.dgis)
        # Выполняем запрос с помощью библиотеки requests и преобразуем JSON-ответ в словарь dict
        total_result = requests.get(request_url).json()
        # Проверяем, есть ли в ответе искомый тег
        if self.has_necessary_filter(total_result, tag):
            count = total_result['result']['total']
            # Расчёт количества страничных запросов
            if count > 50:
                pages = 6
            else:
                pages = math.ceil(count / 10) + 1
            founded = False
            # Проходимся по всем найденным объектам и формируем запрос по каждому из них для поиска объекта с искомым тегом
            for item in total_result['result']['items']:
                # Формирование строки запроса конкретной точки сбора отходов
                request_url = "https://catalog.api.2gis.com/3.0/items?q=раздельный сбор мусора и отходов&lat={}&lon={}&fields=filters&radius=10&key={}".format(
                    item['point']['lat'], item['point']['lon'], self.dgis)
                # Выполняем запрос с помощью библиотеки requests и преобразуем JSON-ответ в словарь dict
                local_result = requests.get(request_url).json()
                # Проверяем, есть ли в ответе искомый тег и нет тега ограничения доступности
                if self.has_necessary_filter(local_result, tag) and \
                        not self.has_necessary_filter(local_result, stop_tag):
                    # Если это так, то запоминаем координаты
                    result_lat = item['point']['lat']
                    result_lon = item['point']['lon']
                    founded = True
                    break
            else:
                # Если на 1 странице не нашли искомую точку, проходимся по остальным страницам
                for i in range(2, pages):
                    # Строка запроса ближайших точек сбора отходов в радиусе 300 метров (i-ая страница)
                    request_url = "https://catalog.api.2gis.com/3.0/items?q=раздельный сбор мусора и отходов&fields=items.point,filters&sort=distance&lon={}&lat={}&radius={}&work_time=now&page={}&key={}" \
                        .format(message.location.longitude, message.location.latitude, radius, i, self.dgis)
                    # Выполняем запрос и преобразуем JSON-ответ в словарь dict
                    total_result = requests.get(request_url).json()
                    for item in total_result['result']['items']:
                        # Формирование строки запроса конкретной точки сбора отходов
                        request_url = "https://catalog.api.2gis.com/3.0/items?q=раздельный сбор мусора и отходов&lat={}&lon={}&fields=filters&radius=10&key={}".format(
                            item['point']['lat'], item['point']['lon'], self.dgis)
                        # Выполняем запрос с помощью библиотеки requests и преобразуем JSON-ответ в словарь dict
                        local_result = requests.get(request_url).json()
                        # Проверяем, есть ли в ответе искомый тег, если есть, то найденные координаты запоминаем
                        if self.has_necessary_filter(local_result, tag) and \
                                not self.has_necessary_filter(local_result, stop_tag):
                            result_lat = item['point']['lat']
                            result_lon = item['point']['lon']
                            founded = True
                            break
                    if founded:
                        break
            # Если нашли объект, то отправляем пользователю геолокацию
            if founded:
                self.bot.send_location(message.chat.id, latitude=result_lat, longitude=result_lon)
            # Такого быть не может, но нужно быть готовым
            else:
                self.bot.send_message(message.chat.id, "Непредвиденная ошибка!")
        # Если среди всей выборки не находим точек с нужным тегом, то отправляем сообщение о неудаче
        else:
            self.bot.send_message(message.chat.id, "Поблизости нет нужной точки")

    def has_necessary_filter(self, result, tag):
        """
        Метод поиска необходимой категории мусора в JSON-ответе от 2ГИС Places API
        :param result: JSON-ответ от 2ГИС Places API
        :param tag: Вид отходов
        :return: True - если тег найден, False - не найден
        """
        for attrs_dicts in result['result']['filters']['attributes']:
            if attrs_dicts['tag'] == tag:
                return True
        return False

    def handle(self):
        """
        Метод переопределяет абстрактный слушатель
        для обработки всех текстовых сообщений
        """

        # Обрабатываем тип сообщений с текстом
        @self.bot.message_handler(func=lambda message: True, content_types=['text'])
        def text_answer(message):
            # обработка кнопок главного меню
            if message.text == config.KEYBOARD['ABOUT_US']:
                self.pressed_btn_about_us(message)

            elif message.text == config.KEYBOARD['BACK_TO_MENU']:
                self.pressed_btn_back(message)

            elif message.text == config.KEYBOARD['GLASS']:
                self.pressed_btn_glass(message)
                self.category = 'glass'

            elif message.text == config.KEYBOARD['PAPER']:
                self.pressed_btn_paper(message)
                self.category = 'paper'

            elif message.text == config.KEYBOARD['PLASTIC']:
                self.pressed_btn_plastic(message)
                self.category = 'plastic'

            elif message.text == config.KEYBOARD['METAL']:
                self.pressed_btn_metal(message)
                self.category = 'metal'

            elif message.text == config.KEYBOARD['BULB']:
                self.pressed_btn_bulb(message)
                self.category = 'bulb'

            elif message.text == config.KEYBOARD['TETRAPAK']:
                self.pressed_btn_tetrapak(message)
                self.category = 'tetrapak'

            elif message.text == config.KEYBOARD['BATTERY']:
                self.pressed_btn_battery(message)
                self.category = 'battery'

            # обработка кнопок подменю в категории "Стекло"

            elif message.text == config.KEYBOARD['ACCEPTED_GLASS']:
                self.pressed_btn_accepted_glass(message)
            elif message.text == config.KEYBOARD['REJECTED_GLASS']:
                self.pressed_btn_rejected_glass(message)
            elif message.text == config.KEYBOARD['PREPARATION_GLASS']:
                self.pressed_btn_preparation_glass(message)
            elif message.text == config.KEYBOARD['MEANING_GLASS']:
                self.pressed_btn_meaning_glass(message)

            # обработка кнопок подменю в категории "Бумага"

            elif message.text == config.KEYBOARD['ACCEPTED_PAPER']:
                self.pressed_btn_accepted_paper(message)
            elif message.text == config.KEYBOARD['REJECTED_PAPER']:
                self.pressed_btn_rejected_paper(message)
            elif message.text == config.KEYBOARD['PREPARATION_PAPER']:
                self.pressed_btn_preparation_paper(message)
            elif message.text == config.KEYBOARD['MEANING_PAPER']:
                self.pressed_btn_meaning_paper(message)

            # обработка кнопок подменю в категории "Пластик"

            elif message.text == config.KEYBOARD['ACCEPTED_PLASTIC']:
                self.pressed_btn_accepted_plastic(message)
            elif message.text == config.KEYBOARD['REJECTED_PLASTIC']:
                self.pressed_btn_rejected_plastic(message)
            elif message.text == config.KEYBOARD['PREPARATION_PLASTIC']:
                self.pressed_btn_preparation_plastic(message)
            elif message.text == config.KEYBOARD['MEANING_PLASTIC']:
                self.pressed_btn_meaning_plastic(message)

            # обработка кнопок подменю в категории "Металл"

            elif message.text == config.KEYBOARD['ACCEPTED_METAL']:
                self.pressed_btn_accepted_metal(message)
            elif message.text == config.KEYBOARD['REJECTED_METAL']:
                self.pressed_btn_rejected_metal(message)
            elif message.text == config.KEYBOARD['PREPARATION_METAL']:
                self.pressed_btn_preparation_metal(message)
            elif message.text == config.KEYBOARD['MEANING_METAL']:
                self.pressed_btn_meaning_metal(message)

            # обработка кнопок подменю в категории "Лампочки"
            elif message.text == config.KEYBOARD['ACCEPTED_BULB']:
                self.pressed_btn_accepted_bulb(message)
            elif message.text == config.KEYBOARD['PREPARATION_BULB']:
                self.pressed_btn_preparation_bulb(message)
            elif message.text == config.KEYBOARD['MEANING_BULB']:
                self.pressed_btn_meaning_bulb(message)

            # обработка кнопок подменю в категории "Тетрапак"

            elif message.text == config.KEYBOARD['ACCEPTED_TETRAPAK']:
                self.pressed_btn_accepted_tetrapak(message)
            elif message.text == config.KEYBOARD['PREPARATION_TETRAPAK']:
                self.pressed_btn_preparation_tetrapak(message)
            elif message.text == config.KEYBOARD['MEANING_TETRAPAK']:
                self.pressed_btn_meaning_tetrapak(message)

            # обработка кнопок подменю в категории "Батарейки"

            elif message.text == config.KEYBOARD['ACCEPTED_BATTERY']:
                self.pressed_btn_accepted_battery(message)
            elif message.text == config.KEYBOARD['PREPARATION_BATTERY']:
                self.pressed_btn_preparation_battery(message)
            elif message.text == config.KEYBOARD['MEANING_BATTERY']:
                self.pressed_btn_meaning_battery(message)
            else:
                self.bot.send_message(message.chat.id, MESSAGES['other_commands'])

        # Обрабатываем тип сообщений с геолокацией
        @self.bot.message_handler(func=lambda message: True, content_types=['location'])
        def location(message):
            if self.category == 'glass':
                self.pressed_btn_location_glass(message)
            elif self.category == 'paper':
                self.pressed_btn_location_paper(message)
            elif self.category == 'plastic':
                self.pressed_btn_location_plastic(message)
            elif self.category == 'metal':
                self.pressed_btn_location_metal(message)
            elif self.category == 'bulb':
                self.pressed_btn_location_bulb(message)
            elif self.category == 'tetrapak':
                self.pressed_btn_location_tetrapak(message)
            elif self.category == 'battery':
                self.pressed_btn_location_battery(message)
            else:
                self.bot.send_message(message.chat.id, MESSAGES['other_commands'])
