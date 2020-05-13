import requests as req
import bs4
import constants as const
from random import randint

# import database as db


class vk_bot:
    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMAND = ['помощь', 'start начать']
        """ Описание для списков ответов на привет и пока
        [0] - длина всего списка
        [1] - [3] - ответы, если человек много раз подряд поприветствовался/попрощался
        [4] - [до конца] - Разные приветствия/прощания
        """
        self._DESCRIPTION = ['Команды:\n',
                             '— псевдоним - изменить обращение. Пример: псевдоним Вася Пупкин\n',
                             '— фото - прислать рандомную фотку из паблика\n',
                             '— топ N - прислать N самых отлайканных записей (максимум 30)(вместо N - любое число). Пример: топ 3']

    def _get_user_name_from_vk_id(self, user_id):
        request = req.get('https://vk.com/id' + str(user_id))
        bs = bs4.BeautifulSoup(request.text, 'html.parser')

        user_name = self._clean_all_tag_from_str(bs.findAll('title')[0])
        user_name_finite = user_name.split()[0]

        return user_name_finite

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        result = ''
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == '<':
                    not_skip = False
                else:
                    result += i
            else:
                if i == '>':
                    not_skip = True

        return result

    def new_message(self, message):
        result = ''
        full_message = message.split()
        message = full_message[0]

        # Использую цикл для того, чтобы не подключать библиотеку goto ради одного выхода
        for need_param in range(1):
            if message.lower() == self._COMMAND[0]:
                for i in range(len(self._DESCRIPTION)):
                    result += self._DESCRIPTION[i]
            elif message.lower() == self._COMMAND[1][0:5]:
                result = 'Привет! Я бот, собирающий статистику по короновирусу' \
                         ' в основном по России (Посмотри команды, написав \'помощь\')'
            elif message.lower() == self._COMMAND[1][6:12]:
                result = 'Привет! Я бот, собирающий статистику по короновирусу' \
                         ' в основном по России (Посмотри команды, написав \'помощь\')'
            else:
                result += 'Извини ' + self._USERNAME + ', я не понимаю тебя. \nПосмотри команды, написав \'помощь\''

        return result
