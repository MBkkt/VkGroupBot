from logging import getLogger

errors = getLogger('errors')


def run_bot():
    try:
        from bot.flask_app import app
        app.run()
    except Exception as e:
        errors.error(str(e))


if __name__ == '__main__':
    run_bot()
else:
    errors.info('No main')
