from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name = 'login_view'),
    path('signup/', views.signup, name= 'signup'),
    path('view_supplier', views.view_supplier, name='view_supplier'),
    path('view_bottles', views.view_bottles, name='view_bottles'),
    path('add_bottle/', views.add_bottle, name='add_bottle'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('delete_account/<int:pk>/', views.delete_account, name='delete_account'),
    path('change_password/<int:pk>/', views.change_password, name='change_password')
]