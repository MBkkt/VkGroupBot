from bot.flask_app import app
from tools.save import Saver

if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        Saver().log(str(e))
else:
    Saver().log('Not main')
