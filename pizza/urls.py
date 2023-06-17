from django.urls import path
from pizza import views

app_name = 'pizza'
urlpatterns = [
    path('', views.list_pizza, name='list_pizza'),
]