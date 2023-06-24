from django.urls import path
from pizza import views

app_name = 'pizza'

urlpatterns = [
    path('', views.list_pizza, name='list_pizza'),
    path('details/<int:pk>/', views.pizza_detail, name='detail'),
    path('add-pizza/', views.add_pizza, name='add_pizza'),
    path('update/<int:pk>/', views.update_pizza, name='update'),
    path('delete/<int:pk>/', views.delete_pizza, name='delete'),
]