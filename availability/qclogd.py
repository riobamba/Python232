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


def main():
  funcionamiento("stations.json")



sched = BlockingScheduler()
sched.add_job(main, 'cron', hour=00, minute=05)
sched.start()



