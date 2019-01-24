from bot.flask_app import app
from tools.save import SAVER

if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        SAVER.log(str(e))
else:
    SAVER.log('Not main')
