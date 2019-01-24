import random
from vk_api import VkApi

from bot.parse import Parser
from config import CONFIG
from tools.save import Saver

VK = VkApi(token=CONFIG.token).get_api()


class Command:
    def __init__(self, event):
        self.user_id = event.object.from_id
        self.type_msg = event.type
        self.user_msg = event.object.text
        self.random_id = random.randint(-4294967296, 4294967295)  # int32
        self.ans_text = {
            'hi': (
                ''
            ),
            'bye': (
                ''
            ),
            'help': (
                ''
            ),
            'faq': (
                ''
            ),
            'product': (
                ''
            ),
            'report': (
                ''
            ),
            'advert': (
                ''
            ),
        }

    def new_msg(self):
        self.type_msg = Parser().parse_msg(self.user_msg)

    def send_msg(self):
        self._send(self.ans_text[self.type_msg])
        if self.type_msg in ('report', 'advert'):
            self._save()

    def _send(self, text):
        VK.messages.send(
            user_id=self.user_id,
            random_id=self.random_id,
            message=text,
        )

    def _save(self):
        Saver().msg(self.type_msg, self.user_msg, self.user_id)
