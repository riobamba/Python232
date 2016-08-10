import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import sqlite3
from datetime import datetime, timedelta


def verificar():
    conn = sqlite3.connect('latency.sqlite')
    latencia = conn.cursor()
    cursor = conn.cursor()
    estacion = conn.cursor()
    fecha_actual = datetime.now()
    minutos = timedelta(seconds=15)
    fecha_atras = fecha_actual - minutos
    print('Tick! Verificador Tiempo de Ejecucion: %s' % datetime.now())
    latencia.execute(("select estacion, valor, estacion_id, fecha from service_latencia sl inner join  service_estacion se on se.id=sl.estacion_id  and fecha BETWEEN '%s' AND '%s' order by estacion_id")%(fecha_atras,fecha_actual))
    estacion.execute(("select estado,fecha,estacion_id from service_estado where  fecha BETWEEN '%s' AND '%s' order by estacion_id")%(fecha_atras,fecha_actual))

    #print ("select estacion, valor, estacion_id, fecha from service_latencia sl inner join  service_estacion se on se.id=sl.estacion_id  and fecha BETWEEN '%s' AND '%s' order by estacion_id")%(fecha_atras,fecha_actual)
    #print ("select estado,fecha,estacion_id from service_estado where  fecha BETWEEN '%s' AND '%s' order by estacion_id")%(fecha_atras,fecha_actual)

    cursor_estado = estacion.fetchall()
    cursor_latencia= latencia.fetchall()
    datos_estado =len(cursor_estado)
    print datos_estado
    if datos_estado > 0 :
        for i in cursor_latencia:
            for j in cursor_estado:
                if i[2]==j[2]:
                    cursor.execute("UPDATE service_estado SET estado='%s',fecha='%s' WHERE estacion_id=%s;" %(cambio(estado(float(i[1])),j[0]), datetime.now(), i[2]))
    else:
        cursor.execute('''delete from service_estado''')
        conn.commit()
        for i in cursor_latencia:
            cursor.execute('''INSERT INTO service_estado (estado,fecha,estacion_id) VALUES(?,?,?)''',(estado(float(i[1])), datetime.now(),i[2]))

    conn.commit()
    conn.close()



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

"""
#verificar()

sched = BlockingScheduler()
sched.add_job(verificar, 'interval', seconds=30)
sched.start()

"""