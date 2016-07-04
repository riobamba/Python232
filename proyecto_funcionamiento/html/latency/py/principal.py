import sys
import consultarsnc
from datetime import datetime,timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os


def funcionamiento(entrada):
  hoy = datetime.now()
  dias = timedelta(days=-1)
  ayer = hoy+dias
  fecha= ayer.strftime("%Y-%m-%d")
  print fecha
  app=consultarsnc.WfqQuery(len(sys.argv), sys.argv, fecha,entrada)
  app()


def main1():
  funcionamiento("stations.json")
  funcionamiento("staacel.json")
  funcionamiento("stainter.json")


sched = BlockingScheduler()
sched.add_job(main1, 'cron', hour=00, minute=05)
sched.start()

def tick():
    print('Corriendo : %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=60)
    scheduler.start()

