from django.conf.urls import url
from .views import elfinder, elfinder_connector

urlpatterns = [
    url(r'^elfinder/$', elfinder, name='cked_elfinder'),
    url(r'^elfinder/connector/$', elfinder_connector, name='cked_elfinder_connector'),
    ]
