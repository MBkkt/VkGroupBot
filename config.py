from collections import namedtuple

CONFIG = namedtuple('config', ('token', 'group_id', 'confirmation', 'api_vk'))(
    token='токен от вашей группы на доступ к сообщениям',
    group_id='int id вашей группы',
    confirmation='ваш код',
    api_vk='5.92',
)
