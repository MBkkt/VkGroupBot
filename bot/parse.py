class Parser:
    msg_words = {
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
    }
    noncallable = (
        '',
    )

    @classmethod
    def parse_msg(cls, text: str) -> str:
        words = text.strip().lower().split()
        if words[0] in cls.noncallable:
            return ''
        for word in words:
            for command_name in cls.msg_words:
                if word in cls.msg_words[command_name]:
                    return command_name
        return 'hi'
