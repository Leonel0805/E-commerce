from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('agregar_producto/<int:producto_id>', views.agregar_producto, name='agregar-producto'),
    path('restar_producto/<int:producto_id>', views.restar_producto, name='restar-producto'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar-carrito'),
    
    
    
]