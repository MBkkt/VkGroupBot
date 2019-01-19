from collections import namedtuple

Config = namedtuple('config', ('token', 'group_id'))

Config = Config(
    token='токен от вашей группы на доступ к сообщениям',
    group_id='int id вашей группы'
)
