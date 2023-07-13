from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User

class Pedido(models.Model):
    ESTADOS_CHOICES = (
        ('en_proceso', 'En preceso'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
        
    )
    
    METODO_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('tarjeta_credito', 'Tarjeta Credito'),
        ('tarjeta_debito', 'Tarjeta Debito'),
        ('paypal', 'Paypal')
    )
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='en_proceso')
    metodo_pago = models.CharField(max_length=20, choices=METODO_CHOICES)
   # total = modelds.
    created = models.DateTimeField(auto_now_add=True) 
       
       
    def __str__(self):
        return f'Pedido #{self.id}'