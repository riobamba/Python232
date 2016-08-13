from django.conf.urls import url
from service import views
from service.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^latencia/$', views.service_list),
    url(r'^historial/$', views.service_historial),
    url(r'^historial2/$', views.service_historial_utimos),
]