from django.conf.urls import url
from service import views

urlpatterns = [
    url(r'^service/$', views.service_list),
    url(r'^service/(?P<fecha>[0-9]{4}[-][0-9]{2}[-][0-9]{2})/$', views.service_detail),
]