command_to_synonym = {
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
synonym_to_command = {
    synonym: command_name
    for command_name, synonym in command_to_synonym.items()
}
noncallable = (
    '',
)


def parse_msg(text: str) -> str:
    words = text.strip().lower().split()
    if words[0] in noncallable:
        return ''
    for word in words:
        if word in synonym_to_command:
            return synonym_to_command[word]
    return 'hi'
