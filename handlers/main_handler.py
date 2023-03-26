# импортируем все виды обработчиков
from handlers.commands_handler import CommandsHandler
from handlers.text_handler import TextHandler


class MainHandler:
    """
    Класс, инициализирующий и запускающий все виды обработчиков
    """

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем все обработчики
        self.handler_commands = CommandsHandler(self.bot)
        self.handler_text = TextHandler(self.bot)

    def handle(self):
        # запускаем все обработчики
        self.handler_commands.handle()
        self.handler_text.handle()
