from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name= 'categoria'
        verbose_name_plural = 'categorias'
        
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name= 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre