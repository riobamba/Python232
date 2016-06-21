import sys
import consultarsnc
from datetime import datetime,timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os


def funcionamiento(entrada,fecha):
  #hoy = datetime.now()
  #dias = timedelta(days=-1)
  #ayer = hoy+dias
  #fecha= ayer.strftime("%Y-%m-%d")
  print fecha
  app=consultarsnc.WfqQuery(len(sys.argv), sys.argv, fecha,entrada)
  app()


def main1():
  hoy = datetime.now()
  dias = timedelta(days=-173)
  ayer = hoy+dias
  
  for x in xrange(1,174):
    d = timedelta(days=+x)
    ayer1=ayer+d
    fecha= ayer1.strftime("%Y-%m-%d")
    funcionamiento("stations.json",fecha)
    funcionamiento("staacel.json",fecha)
    funcionamiento("stainter.json",fecha)


#sched = BlockingScheduler()
#sched.add_job(main1, 'cron', hour=05, m17nute=25)
#sched.start()

main1()


