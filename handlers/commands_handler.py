# импортируем абстрактный класс-обработчик
from handlers.abstract_handler import Handler
# импортируем словарь сообщений от бота пользователю
from settings.message import MESSAGES


class CommandsHandler(Handler):
    """
    Класс обрабатывает входящие команды вида /start и /help
    """

    # инициализируем бота
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        """
        Метод обрабатывает входящие /start команды
        :param message: Входящее сообщение
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['start_message'].format(message.from_user.first_name),
                              parse_mode="HTML",
                              reply_markup=self.keyboards.main_menu())

    def pressed_btn_help(self, message):
        """
               Метод обрабатывает входящие /help команды
               :param message: Входящее сообщение
               """
        self.bot.send_message(message.chat.id,
                              MESSAGES['help_message'].format(message.from_user.first_name),
                              parse_mode="HTML",
                              reply_markup=self.keyboards.main_menu())

    def handle(self):
        """
        Метод переопределяет абстрактный слушатель
        для обработки команды /start
        """
        @self.bot.message_handler(commands=['start', 'help'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)
            elif message.text == '/help':
                self.pressed_btn_help(message)
