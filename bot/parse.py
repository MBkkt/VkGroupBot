class Parser:
    def __init__(self):
        self.msg_words = {
            'hi': (
                'hi', 'hello', 'goodmorning', 'about',
                'привет', 'здраствуй', 'здраствуйте', 'ку', 'здаров', 'прив', 'хай',
            ),

            'report': (
                'report', 'репорт'
            ),

            'product': (
                'product', 'products', 'buy',
                'купить', 'товары', 'товар', 'продукты', 'продукт',
            ),

            'help': (
                'help', 'command', 'commands',
                'помощь', 'помогите', 'команды', 'команда',
            ),
            'faq': (
                'faq', 'инструкция',
            ),

            'advert': (
                'advert', 'реклама'
            ),
            'noncallable': (
                'команда другого вашего бота например'
            ),
        }

    def parse_msg(self, text: str):
        words = text.strip().lower().split()
        if words[0] in self.msg_words['noncallable']:
            return None
        for word in words:
            if word in self.msg_words['hi']:
                return 'hi'
            if word in self.msg_words['report']:
                return 'report'
            if word in self.msg_words['product']:
                return 'product'
            if word in self.msg_words['help']:
                return 'help'
            if word in self.msg_words['faq']:
                return 'faq'
            if word in self.msg_words['advert']:
                return 'advert'
        return 'hi'
