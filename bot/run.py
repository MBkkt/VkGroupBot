from vk_api.bot_longpoll import VkBotEventType

from bot import longpoll
from bot.command import Command
from bot.parse import parseMessage


def run():
    for event in longpoll.listen():
        command = Command(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            event = parseMessage(event.obj.text)
            if event is None:
                continue

            elif event == 'hello':
                command.hi()

            elif event == 'product':
                command.product()

            elif event == 'help':
                command.help()

            elif event == 'report':
                command.report()

            elif event == 'faq':
                command.faq()

            elif event == 'advert':
                command.advert()

        elif event.type == VkBotEventType.GROUP_JOIN:
            # command.hi()
            pass

        elif event.type == VkBotEventType.GROUP_LEAVE:
            # command.bye()
            pass
