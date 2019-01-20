from bot import run


def app_run():
    while True:
        try:
            run.run()
        except Exception as e:
            with open('/home/MBkkt/VkSupremeGroupBot/data/log.txt', 'a') as log_file:
                log_file.write(str(e) + '\n\n')


app_run()
