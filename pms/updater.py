from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from . import update_salary

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_salary.update, 'interval',minutes=1)
    print("GO")
    scheduler.start()