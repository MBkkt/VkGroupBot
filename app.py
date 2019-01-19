from flask import Flask

from bot import run


def app_run():
    try:
        run.run()
    except Exception as e:
        with open('data/log.txt', 'a') as log_file:
            print(e)
            log_file.write(str(e) + '\n\n')


app_run()

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def about_me():
    return "Bot by MBkkt"
