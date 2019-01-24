from flask import Flask, request, json, abort, make_response, jsonify
from vk_api.bot_longpoll import VkBotEventType, VkBotEvent

from bot.command import Command
from config import CONFIG
from tools.save import Saver

app = Flask(__name__)


@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found this url'}), 404)


@app.route('/')
def hello_world():
    return 'VKGroupBot by MBkkt'


@app.route('/bot', methods=['POST'])
def processing():
    event = json.loads(request.data)
    try:
        if event['type'] == 'confirmation':
            return CONFIG.confirmation
        event = VkBotEvent(event)
        command = Command(event)
    except Exception as e:
        Saver().log(str(e))
        abort(400)
    else:
        if event.type == VkBotEventType.MESSAGE_NEW:
            command.new_msg()
            if command.type_msg is not None:
                command.send_msg()
        elif event.type == VkBotEventType.GROUP_JOIN:
            command.type_msg = 'hi'
            command.send_msg()
        elif event.type == VkBotEventType.GROUP_LEAVE:
            command.type_msg = 'bye'
            command.send_msg()
        return 'ok'
