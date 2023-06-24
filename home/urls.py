from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home')
    #path('search/', views.search_pizza, name='search_pizza')
]