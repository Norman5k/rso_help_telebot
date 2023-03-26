# импортируем библиотеку abc для реализации абстрактных классов
import abc
# импортируем разметку клавиатуры и клавиш
from markup.markup import Keyboards
# импортируем созданную конфигурацию
from settings import config


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем разметку кнопок
        self.keyboards = Keyboards()
        # инициализируем токен 2Гис
        self.dgis = config.MAP_TOKEN

    # абстрактный метод-обработчик
    @abc.abstractmethod
    def handle(self):
        pass
