from django.urls import path
from . import views


urlpatterns = [
    path('view_supplier', views.view_supplier, name='view_supplier'),
    path('view_bottles', views.view_bottles, name='view_bottles'),
    path('add_bottle', views.add_bottle, name='add_bottle')
]