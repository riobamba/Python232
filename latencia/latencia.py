import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import sqlite3
from time import strftime
from datetime import datetime, timedelta

def main():
    cliente()

def cliente():
    conn = sqlite3.connect('latency.sqlite')
    estacion = conn.cursor()
    estacion.execute("select id,estacion from service_estacion")
    #print('\nTick! Cliente Tiempo de Ejecucion: %s' % datetime.now())
    url = "http://10.100.100.232:8081/query/objects.json?QC&last=%s" % (time.strftime("%Y%m%d.%H%M%S", time.localtime()))
    #print url
    latencia = dict()
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        for row in estacion:
            band=True
            sta = dict()
            for result in results['request']['QC']['list']:
               station = result['id'].split('.')
               if station[1] == row[1]:
                  band=False
                  sta['valor']=result['params']['latency']['value']
                  timestamp = str(result['params']['latency']['timestamp'])
                  sta['fecha']=datetime.fromtimestamp(int(timestamp[0:10])).strftime('%Y-%m-%d %H:%M:%S')
                  sta['id_estacion']=row[0]
            if band :
                sta['valor'] = -1
                sta['fecha'] = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
                sta['id_estacion'] = row[0]
            latencia[row[0]]=sta
    else:
        print "Error code %s" % response.status_code
    verificar(latencia)
    conn.close()


def verificar(latencia):
    conn = sqlite3.connect('latency.sqlite')
    cursor = conn.cursor()
    estacion = conn.cursor()
    #print('\nTick! Verificador Tiempo de Ejecucion: %s' % datetime.now())
    estacion.execute("select valor,fecha,estacion_id from service_estado order by estacion_id")
    cursor_estado = estacion.fetchall()
    datos_estado =len(cursor_estado)
    #print datos_estado
    if datos_estado > 0 :
        for i in latencia:
            data = latencia[i]
            for j in cursor_estado:
                if data['id_estacion']==j[2]:
                    cursor.execute("UPDATE service_estado SET valor='%s',fecha='%s' WHERE estacion_id=%s;" %(cambio(estado(data['valor']),j[0]),data['fecha'],data['id_estacion']))
    else:
        cursor.execute('''delete from service_estado''')
        conn.commit()
        for i in latencia:
            data = latencia[i]
            cursor.execute('''INSERT INTO service_estado (valor,fecha,estacion_id) VALUES(?,?,?)''',(estado(float(data['valor'])), data['fecha'],data['id_estacion']))
    conn.commit()
    conn.close()
    estados()




def estado(val):
    if val > 0 and val < 90:
        return "ok"
    elif val > 90 or val < 0:
        return "fuera"

def cambio(actual, anterior):
    if actual==anterior:
        return actual
    elif actual=="ok" and  anterior=="fuera":
        return "entra"
    elif actual=="ok" and anterior=="entra":
        return "ok"
    elif actual=="ok" and anterior=="salio":
        return "entra"
    elif actual=="fuera" and anterior=="ok":
        return "salio"
    elif actual=="fuera" and anterior=="entra":
        return "salio"
    elif actual=="fuera" and anterior=="salio":
        return "fuera"


def estados():
    conn = sqlite3.connect('latency.sqlite')
    estado = conn.cursor()
    cursor = conn.cursor()
    print('\nTick! Estado Tiempo de Ejecucion: %s' % datetime.now())
    estado.execute("select estacion, valor, estacion_id, fecha from service_estado sl inner join  service_estacion se on se.id=sl.estacion_id order by estacion_id")

    cursor_latencia= estado.fetchall()

    for i in cursor_latencia:
        if i[1] == "entra":
            print "Estacion %s Ingresa %s" % (i[0],i[3])
            cursor.execute('''INSERT INTO service_historial (valor,fecha,estacion_id) VALUES(?,?,?)''',('in',i[3] , i[2]))
            conn.commit()
        elif i[1] == "salio":
            print "Estacion %s Sale %s" % (i[0],i[3])
            cursor.execute('''INSERT INTO service_historial (valor,fecha,estacion_id) VALUES(?,?,?)''',('out', i[3], i[2]))
            conn.commit()

    conn.close()



sched = BlockingScheduler()
sched.add_job(main, 'interval', seconds=10)
sched.start()