from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(schedule_api,'interval',minutes=1)
    scheduler.start()
    