from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from service.models import Estacion
from django.db import connection
import json
from django.shortcuts import render,redirect
from datetime import datetime, timedelta


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
        
@csrf_exempt
def service_list(request):
    """
    Retorna todos los registros de la tabal estado.
    """
    try:
        datos=[]
        cursor = connection.cursor()
        cursor.execute("select estacion,latitud,longitud, valor, fecha from service_estado sl inner join  service_estacion se on se.id=sl.estacion_id ")
        for row in cursor:
          est= {"estacion":row[0], "latitud":row[1], "longitud":row[2], "valor":row[3], "fecha":str(row[4]) }
          datos.append(est)
        resp=json.loads(json.dumps(datos,ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)

@csrf_exempt
def service_historial(request):
    """
    Retorna los ultimos 12 registros de la tabal historial.
    """
    try:
        datos=[]
        cursor = connection.cursor()
        cursor.execute("select estacion, valor, fecha from service_historial sl inner join  service_estacion se on se.id=sl.estacion_id order by fecha desc limit 10 ")
        for row in cursor:
          est= {"estacion":row[0], "valor":row[1], "fecha":str(row[2]) }
          datos.append(est)
        resp=json.loads(json.dumps(datos,ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)

def service_historial_utimos(request):
    """
    Retorna los ultimos registros de la tabal historial.
    """
    fecha_actual = datetime.now()
    segundos = timedelta(seconds=60)
    fecha_atras = fecha_actual - segundos
    try:
        datos=[]
        cursor = connection.cursor()
        #cursor.execute(("select estacion, valor, fecha, administrador from service_historial sl inner join  service_estacion se on se.id=sl.estacion_id and fecha BETWEEN '%s' AND '%s'  order by fecha desc  limit 10")%(fecha_atras,fecha_actual))
        cursor.execute("select estacion, valor, fecha, administrador from service_historial sl inner join  service_estacion se on se.id=sl.estacion_id and administrador not like 'INTER'  order by fecha desc limit 10")
        for row in cursor:
          est= {"estacion":row[0], "valor":row[1], "fecha":str(row[2]),"admin":row[3] }
          datos.append(est)
        resp=json.loads(json.dumps(datos,ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)

        
def index(request):
    return render(request,'service/index.html')