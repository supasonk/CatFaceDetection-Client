from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^detect/$', views.detect, name='detect'),
]
