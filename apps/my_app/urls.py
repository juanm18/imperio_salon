from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^servicios$', service, name="services"),
    url(r'^contactenos$', contact, name="contact"),
]
