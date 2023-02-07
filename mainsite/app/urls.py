from django.urls import path
from . import views

urlpatterns = [
    path('echo', views.echo, name='echo'),
    path('invert', views.invert, name='invert'),
    path('flatten', views.flatten, name='flatten'),
    path('sum', views.sum, name='sum'),
    path('multiply', views.multiply, name='multiply'),
]