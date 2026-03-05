# slider/urls.py
from django.urls import path
from . import views

app_name = 'slider'

urlpatterns = [
    path('', views.index, name='index'),
]