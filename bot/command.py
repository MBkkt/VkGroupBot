from random import randint

from bot import vk


class Command:
    def __init__(self, event):
        self.user_id = event.object.from_id
        self.user_msg = event.object.text
        self.random_id = randint(1, 10000)

    def _send(self, text):
        vk.messages.send(
            user_id=self.user_id,
            random_id=self.random_id,
            message=text,
        )

    def hi(self):
        text = '''ваш текст'''
        self._send(text)

    def bye(self):
        text = ''''''
        self._send(text)

    def help(self):
        text = ''''''
        self._send(text)

    def faq(self):
        text = ''''''
        self._send(text)

    def product(self):
        text = ''''''
        self._send(text)

    def report(self):
        with open('data/report.txt', 'a') as report_file:
            report_file.write(self.user_msg + f"\nby user: https://vk.com/id{self.user_id}\n\n")
        text = '''Спасибо за это сообщение, мы постараемся это исправить в ближайшее время '''
        self._send(text)

    def advert(self):
        with open('data/advert.txt', 'a') as advert_file:
            advert_file.write(self.user_msg + f"\nby user: https://vk.com/id{self.user_id}\n\n")
        text = '''Мы напишем вам, если нас заинтересует ваше предложение '''
        self._send(text)
