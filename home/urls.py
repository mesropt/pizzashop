from django.urls import path
from home import views

app_name = 'pizza'
urlpatterns = [
    path('', views.home, name='home')
]