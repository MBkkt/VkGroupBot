from datetime import datetime
from os.path import abspath, dirname, join


class Saver:
    def __init__(self):
        self.path = dirname(abspath('app.py'))
        self.text = ''
        self.file = ''

    def _save(self):
        with open(join(self.path, 'data', self.file), 'a') as f:
            f.write(f"{self.text}\n{datetime.now()}\n\n")

    def log(self, text):
        self.text = text
        self.file = 'log.txt'
        self._save()

    def msg(self, type_msg, text, user_id):
        self.text = f'{text}\nby user: https://vk.com/id{user_id}'
        self.file = f'{type_msg}.txt'
        self._save()
