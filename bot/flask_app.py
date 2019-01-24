from flask import Flask, request, json, abort, make_response, jsonify
from vk_api.bot_longpoll import VkBotEventType, VkBotEvent

from bot.command import COMMAND
from tools.save import SAVER
from config import CONFIG

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
    except Exception as e:
        SAVER.log(str(e))
        abort(400)

    COMMAND(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        COMMAND.new_msg()
        if COMMAND.type_msg is not None:
            COMMAND.send_msg()
    elif event.type == VkBotEventType.GROUP_JOIN:
        COMMAND.type_msg = 'hi'
        COMMAND.send_msg()
    elif event.type == VkBotEventType.GROUP_LEAVE:
        COMMAND.type_msg = 'bye'
        COMMAND.send_msg()
    return 'ok'
