from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from service.models import Funcionamiento
from service.models import Estacion
from service.serializers import FuncionamientoSerializer
from service.serializers import EstacionSerializer
from django.db import connection
import json
from django.core import serializers


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
    Retorna todos los registros de la base de datos.
    """
    if request.method == 'GET':
        service = Estacion.objects.all()
        serializer = EstacionSerializer(service, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EstacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
@csrf_exempt
def service_detail(request, fecha):
    """
    Retorna una fecha especifica de la base de datos.
    """
    try:
        datos=[]
        cursor = connection.cursor()
        cursor.execute("SELECT estacion,latitud,longitud,administrador,fecha,valor FROM service_estacion se, service_funcionamiento ss WHERE se.id = ss.estacion_id and ss.fecha='%s' "%fecha)
        for row in cursor:
          est= {"estacion":row[0], "latitud":row[1], "longitud":row[2], "administrador":row[3], "fecha":str(row[4]), "valor":row[5]}
          datos.append(est)
        resp=json.loads(json.dumps(datos,ensure_ascii=False))
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JSONResponse(resp)
