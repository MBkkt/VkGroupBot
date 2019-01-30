from logging import getLogger
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id

from bot.parse import Parser
from config import CONFIG

reports = getLogger('reports')
adverts = getLogger('adverts')

VK = VkApi(token=CONFIG.token).get_api()


class Command:
    ans_text = {
        'hi': (
            'Привет, это бот...'
        ),
        'bye': (
            'Спасибо...'
        ),
        'help': (
            'Список команд: help...'
        ),
        'faq': (
            'FAQ...'
        ),
        'product': (
            'Подробное...'
        ),
        'report': (
            'Спасибо за это сообщение, мы постараемся это... '
        ),
        'advert': (
            'Мы напишем вам, если нас заинтересует...'
        ),
    }

    loggers = {
        'adverts': adverts,
        'report': reports,
    }

    def __init__(self, event):
        self.type_event = event.type
        self.user_id = event.object.from_id
        self.user_msg = event.object.text

        if self.type_event == VkBotEventType.MESSAGE_NEW:
            self.type_msg = Parser.parse_msg(self.user_msg)
        elif self.type_event == VkBotEventType.GROUP_JOIN:
            self.type_msg = 'hi'
        elif self.type_event == VkBotEventType.GROUP_LEAVE:
            self.type_msg = 'bye'
        else:
            self.type_msg = ''

    def send_msg(self):
        if self.type_msg:
            self._send()
        if self.type_msg in Command.loggers:
            self._save()

    def _send(self):
        VK.messages.send(
            user_id=self.user_id,
            random_id=get_random_id(),
            message=Command.ans_text[self.type_msg],
        )

    def _save(self):
        Command.loggers[self.type_msg].info(f'{self.user_msg}\nby user: https://vk.com/id{self.user_id}')
