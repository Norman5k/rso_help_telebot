# импортируем функцию создания объекта бота
from telebot import TeleBot
# импортируем созданную конфигурацию проекта
from settings import config
# импортируем главный класс-обработчик бота
from handlers.main_handler import MainHandler


class TelBot:
    """
    Основной класс Telegram-бот
    """
    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        """
        Метод, инициализацирующий бота
        """
        # Получаем токен
        self.token = config.BOT_TOKEN
        # Инициализируем бота на основе зарегистрированного токена
        self.bot = TeleBot(self.token)
        # Инициализируем все обработчики событий
        self.handler = MainHandler(self.bot)

    def run_bot(self):
        """
        Метод запускает основные события сервера
        """
        # Запуск обработчиков событий
        self.handler.handle()
        # Запуск бота в режиме нон-стоп
        self.bot.polling(none_stop=True)


# Точка входа приложения
if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
