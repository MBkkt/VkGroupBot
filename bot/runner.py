from vk_api.bot_longpoll import VkBotEventType

from bot import longpoll
from bot.command import Command
from bot.parse import parseMessage


def run():
    command = Command()
    for event in longpoll.listen():
        command(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg_type = parseMessage(event.obj.text)
            if msg_type is not None:
                command.sendMsg(msg_type)

        elif event.type == VkBotEventType.GROUP_JOIN:
            command.sendMsg('hi')

        elif event.type == VkBotEventType.GROUP_LEAVE:
            command.sendMsg('bye')
