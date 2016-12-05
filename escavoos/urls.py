"""Define padrões de URL para escavoos"""

from django.conf.urls import url
from escavoos.views import index, escavoo


urlpatterns = [
    # página inicial
    url(r'^$', index, name='index'),
    url(r'^escavoo/$', escavoo, name='escavoo'),
]