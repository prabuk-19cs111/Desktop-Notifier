import time
import schedule

def timeschedule(x):

    def job():
        exec(open('notifier.py').read())

    schedule.every().day.at(x).do(job)


    while True:
        schedule.run_pending()
        time.sleep(1)
        