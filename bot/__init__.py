from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll

from config import Config

vk_session = VkApi(token=Config.token)
longpoll = VkBotLongPoll(vk_session, group_id=Config.group_id)
vk = vk_session.get_api()
