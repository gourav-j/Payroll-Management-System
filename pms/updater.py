from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from . import update_salary

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_salary.update, 'cron',day_of_week='mon',day='1st mon')
    scheduler.start()