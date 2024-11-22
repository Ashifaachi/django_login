from django.contrib import admin
from django.urls import path,include
from . import views
app_name='app1'
urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login,name='login'),
    path('gallary/',views.gallary,name='gallary'),
    path('register/',views.register,name='register'),
    path('details/<int:id>/',views.details,name='details'),
  
]
