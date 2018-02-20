from django.conf.urls import url
from . import v1

urlpatterns = [
    url(r'^v1/letniki/$', v1.letniki, name='api_letniki'),
    url(r'^v1/urnik_letnika/$', v1.urnik_letnika, name='api_semester'),
]
