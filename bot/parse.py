def parseMessage(text: str):
    words = text.strip().lower().split()

    if any(word in words[0] for word in ('команда вашего callback бота например',)):
        return None

    for word in words:
        if word in (
                'hi', 'hello', 'goodmorning', 'about',
                'привет', 'здраствуй', 'здраствуйте', 'ку', 'здаров', 'прив', 'хай',):
            return 'hello'

        elif word in ('report', 'репорт'):
            return 'report'

        elif word in (
                'product', 'products', 'buy',
                'купить', 'товары', 'товар', 'продукты', 'продукт',):
            return 'product'

        elif word in (
                'help', 'command', 'commands',
                'помощь', 'помогите', 'команды', 'команда',):
            return 'help'

        elif word in ('faq', 'инструкция',):
            return 'faq'

        elif word in ('advert', 'реклмама'):
            return 'advert'

    return 'hello'
