from django.urls import re_path, include
from . import views
from . views import *
from django.views.generic.detail import DetailView
from personal.models import source, node1, node2, node3

urlpatterns = [
    re_path(r'^$' , views.index, name='index'),
    re_path(r'^TurnOFF1/' , views.TurnOFF1, name='TurnOFF1'),
    re_path(r'^TurnOFF2/' , views.TurnOFF2, name='TurnOFF2'),
    re_path(r'^TurnOFF3/' , views.TurnOFF3, name='TurnOFF3'),
    re_path(r'^TurnOFFS/' , views.TurnOFFS, name='TurnOFFS'),
    re_path(r'^vals/', vals)
]
