import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import sqlite3
from procesa import verificar

def main():
    tick()
    verificar()


def tick():
    conn = sqlite3.connect('latency.sqlite')
    estacion = conn.cursor()
    cursor = conn.cursor()
    estacion.execute("select id,estacion from service_estacion")
    print('Tick! Cliente Tiempo de Ejecucion: %s' % datetime.now())
    url = "http://10.100.100.232:8081/query/objects.json?QC&last=%s" % (time.strftime("%Y%m%d.%H%M%S", time.localtime()))
    print url
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        for row in estacion:
            band=True
            for result in results['request']['QC']['list']:
               station = result['id'].split('.')
               if station[1] == row[1]:
                  band=False
                  cursor.execute('''INSERT INTO service_latencia (valor,fecha,estacion_id) VALUES(?,?,?)''', (result['params']['latency']['value'],datetime.now(),row[0]))
            if band :
               cursor.execute('''INSERT INTO service_latencia (valor,fecha,estacion_id) VALUES(?,?,?)''', ('-1', datetime.now(), row[0]))
        conn.commit()

    else:
        print "Error code %s" % response.status_code

    conn.close()

sched = BlockingScheduler()
sched.add_job(main, 'interval', seconds=10)
sched.start()

