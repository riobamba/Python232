
from apscheduler.schedulers.blocking import BlockingScheduler
from monitor232 import monitor232
from monitor13 import monitor13
import logging

logging.basicConfig()

sched = BlockingScheduler()
sched.add_job(monitor232, 'interval', seconds=60)
sched.add_job(monitor13, 'interval', seconds=60)

sched.start()