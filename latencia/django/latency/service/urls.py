from django.conf.urls import url
from service import views
from service.views import seismo1,xena

urlpatterns = [
    url(r'^seismo1$', seismo1, name='seismo1'),
    url(r'^xena$', xena, name='xena'),
    url(r'^latencia232/$', views.service_list232),
    url(r'^latencia13/$', views.service_list13),
    url(r'^historial/(?P<servidor>[0-9]{3})/$', views.service_historial),
    url(r'^historial2/(?P<servidor>[0-9]{3})/$', views.service_historial_utimos),
]