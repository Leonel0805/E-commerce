from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio-sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar-sesion')
    
    
]