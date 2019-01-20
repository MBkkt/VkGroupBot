from bot import runner


def app_run():
    while True:
        try:
            runner.run()
        except Exception as e:
            with open(r'/absolute/path/to/your/data/log.txt', 'a') as log_file:
                log_file.write(str(e) + '\n\n')


if __name__ == '__main__':
    app_run()
