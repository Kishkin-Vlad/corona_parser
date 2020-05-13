import vk_api
import constants as const
import random
import requests as req

from class_vk_bot import vk_bot

# Авторизация, как сообщества
vk = vk_api.VkApi(token=const.token)
upload = vk_api.VkUpload(vk)

server = ''
key = ''


# Проверка число ли
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Написать сообщение пользователю
"""
write_msg(vk, event.user_id, 'Ответ на привет', random.getrandbits(64))
"""
def write_msg(user_vk, user_id, message, random_id):
    user_vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': random_id
    })

# цикл проверки на события
# + ответ на сообщения (в общем работа бота)
def cycle_connection(ts):
    connection = req.get(f'{server}?act=a_check&key={key}&ts={ts}&wait=25',
                         params={
                             'access_token': const.token,
                             'v': const.version
                         })

    data = connection.json()
    event_type = ''

    # data['updates'] != []. Т.е. Если он не пустой, то выводит это
    try:
        if data['updates']:
            user_id = data['updates'][0]['object']['from_id']
            text = data['updates'][0]['object']['text']
            event_type = data['updates'][0]['type']
    except KeyError:
        print('WORK EXCEPTION KEYERROR')
        cycle_work()
        return
    if event_type == 'message_new':
        print(f'Wrote a message: {user_id}\nMessage: \'{text}\'')
        bot = vk_bot(user_id)
        write_msg(vk, user_id, bot.new_message(text), random.getrandbits(64))

    # Выводит data (инфо о событие) при любом случае, кроме случая когда он сам отправил сообщение
    if event_type != 'message_reply':
        print(data)

    ts = data['ts']
    del data, event_type
    cycle_connection(ts)


# цикличная работа бота (проверка на события и действия бота)
def cycle_work():
    group_get_longPoll = req.get('https://api.vk.com/method/groups.getLongPollServer',
                                 params={
                                     'access_token': const.token,
                                     'v': const.version,
                                     'group_id': const.id_group
                                 })

    data = group_get_longPoll.json()
    global key, server
    key = data['response']['key']
    server = data['response']['server']
    ts = data['response']['ts']

    cycle_connection(ts)
