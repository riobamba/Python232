import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())
    url="http://10.100.100.232:8081/query/objects.json?QC&last=%s" % (time.strftime("%Y%m%d.%H%M%S", time.localtime()))
    print url
    response = requests.get("url")
    if response.status_code == 200:
        results = response.json()
        for result in results['request']['QC']['list']:
            ts = result['params']['latency']['timestamp']
            print result['id'], result['params']['latency']['value'], ts
    else:
        print "Error code %s" % response.status_code



def job_function():
    print("Hello World")

sched = BlockingScheduler()
sched.add_job(tick, 'interval', minutes=1)
sched.start()

