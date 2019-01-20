from random import randint

from bot import vk


class Command:
    def __init__(self):
        self.user_id = 0
        self.user_msg = 0
        self.random_id = 42
        self.dict_text = {
            'hi': (
                ''
            ),
            'bye': (
                ''
            ),
            'help': (
                'Список команд: help \n'
                'О боте: about '
            ),
            'faq': (
                ''
            ),
            'product': (
                ''
            ),
            'report': (
                'Спасибо за это сообщение, мы постараемся это исправить в ближайшее время '
            ),
            'advert': (
                'Мы напишем вам, если нас заинтересует ваше предложение '
            ),
        }

    def __call__(self, event):
        self.user_id = event.object.from_id
        self.user_msg = event.object.text
        self.random_id = randint(1, 10000)

    def _sendToVk(self, text):
        vk.messages.send(
            user_id=self.user_id,
            random_id=self.random_id,
            message=text,
        )

    def sendMsg(self, msg_type):
        self._sendToVk(self.dict_text[msg_type])
        if msg_type in ('report', 'advert'):
            with open(f'/absolute/path/to/your/data/{msg_type}.txt', 'a') as file:
                file.write(self.user_msg + f'\nby user: https://vk.com/id{self.user_id}\n\n')
