from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from service.models import Estacion
from django.db import connection
import json
from django.shortcuts import render, redirect
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
def service_list232(request):
    """
    Retorna todos los registros de la tabal estado.
    """
    try:
        datos = []
        cursor = connection.cursor()
        cursor.execute(
            "select estacion,latitud,longitud, valor, fecha from service_estado232 sl inner join  service_estacion se on se.id=sl.estacion_id ")
        for row in cursor:
            est = {"estacion": row[0], "latitud": row[1], "longitud": row[2], "valor": row[3], "fecha": str(row[4].strftime('%Y-%m-%d %H:%M:%S'))}
            datos.append(est)
        resp = json.loads(json.dumps(datos, ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)


@csrf_exempt
def service_list13(request):
    """
    Retorna todos los registros de la tabal estado.
    """
    try:
        datos = []
        cursor = connection.cursor()
        cursor.execute(
            "select estacion,latitud,longitud, valor, fecha from service_estado13 sl inner join  service_estacion se on se.id=sl.estacion_id ")
        for row in cursor:
            est = {"estacion": row[0], "latitud": row[1], "longitud": row[2], "valor": row[3], "fecha": str(row[4].strftime('%Y-%m-%d %H:%M:%S'))}
            datos.append(est)
        resp = json.loads(json.dumps(datos, ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)


@csrf_exempt
def service_historial(request, servidor):
    """
    Retorna los ultimos 12 registros de la tabal historial.
    """
    try:
        datos = []
        cursor = connection.cursor()
        cursor.execute((
                       "select estacion, valor, fecha from service_historial sl inner join  service_estacion se on se.id=sl.estacion_id and servidor='%s' order by fecha desc limit 10 ") % servidor)
        for row in cursor:
            est = {"estacion": row[0], "valor": row[1], "fecha": str(row[2].strftime('%Y-%m-%d %H:%M:%S'))}
            datos.append(est)
        resp = json.loads(json.dumps(datos, ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)


def service_historial_utimos(request, servidor):
    """
    Retorna los ultimos registros de la tabal historial.
    """
    fecha_actual = datetime.now()
    segundos = timedelta(seconds=60)
    fecha_atras = fecha_actual - segundos
    try:
        datos = []
        cursor = connection.cursor()
        # cursor.execute(("select estacion, valor, fecha, administrador from service_historial sl inner join  service_estacion se on se.id=sl.estacion_id and fecha BETWEEN '%s' AND '%s' order by fecha desc  limit 10")%(fecha_atras,fecha_actual))
        cursor.execute((
                       "select estacion, valor, fecha, administrador from service_historial sl inner join  service_estacion se on se.id=sl.estacion_id and administrador not like 'INTER' and servidor='%s' order by fecha desc limit 10") % servidor)
        for row in cursor:
            est = {"estacion": row[0], "valor": row[1], "fecha": str(row[2].strftime('%Y-%m-%d %H:%M:%S')), "admin": row[3]}
            datos.append(est)
        resp = json.loads(json.dumps(datos, ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)


def seismo1(request):
    return render(request, 'service/seismo1.html')


def xena(request):
    return render(request, 'service/xena.html')

def service_historial_estacion(request):
    if request.method == 'GET':
        servidor = request.GET.get('servidor','')
        estacion = request.GET.get('estacion','')
        if not request.GET.get('servidor', ''):
            servidor = "debe introducir una servidor"
        if not request.GET.get('estacion', ''):
            estacion = "debe introducir una estacion"
        """https://availability-riobamba.c9users.io/service2/?fecha_inicial=2016-05-05&fecha_final=2016-07-07"""
        #sql= "select estacion, valor, fecha from service_estado"+str(servidor)+" s innner_join service_estacion se on s."
        try:
            datos = []
            cursor = connection.cursor()
            print "SELECT estacion, valor, fecha, servidor from service_historial sh inner join service_estacion se on se.id=sl.estacion_id and se.estacion = '%s' and sh.servidor = '%s' order by fecha desc limit 8" % (estacion,servidor)
            cursor.execute("SELECT estacion, valor, fecha, servidor from service_historial sh inner join service_estacion se on se.id=sh.estacion_id and se.estacion = '%s' and sh.servidor = '%s' order by fecha desc limit 10" % (estacion,servidor))
            #cursor_estado = estacion.fetchall()
            #datos_estado = len(cursor_estado)
            for row in cursor:
                #est = {"estacion": row[0], "valor": str(row[1]), "fecha": str(row[2]), "servidor": row[3]}
                est = {"estacion": row[0], "valor": str(row[1]), "fecha": str(row[2].strftime('%Y-%m-%d %H:%M:%S')), "servidor": row[3]}
                #.strftime('%Y-%m-%d %H:%M:%S')
                print est
                datos.append(est)
            resp = json.loads(json.dumps(datos, ensure_ascii=False))
            return JSONResponse(resp)
        except Estacion.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            return JSONResponse(resp)
