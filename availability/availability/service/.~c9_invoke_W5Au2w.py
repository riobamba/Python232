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
    List all code snippets, or create a new snippet.
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
def service_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        #snippet = Snippet.objects.get(pk=pk)
        #para buscar por una tupla en especial
        #service = Funcionamiento.objects.filter(fecha=fecha)
        service = Estacion.objects.filter(funcionamiento=estacion, estacion__funcionamiento__fecha=pk)
    except Estacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EstacionSerializer(service, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EstacionSerializer(service, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        service.delete()
        return HttpResponse(status=204)