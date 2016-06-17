import sys
import consultarsnc
import multiprocessing
from datetime import datetime,timedelta
from apscheduler.schedulers.blocking import BlockingScheduler


def funcionamiento(entrada):
  hoy = datetime.now()
  dias = timedelta(days=-1)
  ayer = hoy+dias
  fecha= ayer.strftime("%Y-%m-%d")
  print fecha
  app=consultarsnc.WfqQuery(len(sys.argv), sys.argv, fecha,entrada)
  app()


def main():
  r = multiprocessing.Process(target=funcionamiento,args=("stations.json"))
  r.start()
  a = multiprocessing.Process(target=funcionamiento,args=("staacel.json"))
  a.start()
  i = multiprocessing.Process(target=funcionamiento,args=("stainter.json"))
  i.start()


sched = BlockingScheduler()
sched.add_job(main, 'cron', hour=00, minute=05)
sched.start()

