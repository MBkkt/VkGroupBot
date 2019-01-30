from flask import Flask, request, json, abort, make_response, jsonify
from logging import getLogger
from vk_api.bot_longpoll import VkBotEvent

from bot.command import Command
from config import CONFIG

errors = getLogger('errors')

app = Flask(__name__)


@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found this url'}), 404)


@app.route('/')
def about():
    return 'VKGroupBot by MBkkt'


@app.route('/bot', methods=['POST'])
def processing():
    try:
        event = json.loads(request.data)
        if event['type'] == 'confirmation':
            return CONFIG.confirmation
        command = Command(VkBotEvent(event))
    except Exception as e:
        errors.error(str(e))
        abort(400)
    else:
        command.send_msg()
        return 'ok'
