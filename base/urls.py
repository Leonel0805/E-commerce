from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('compra_finalizada/', views.finalizar_compra, name='compra-finalizada'),
    
]