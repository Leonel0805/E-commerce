from django.contrib import admin
from .models import Producto, Categoria


#registramos nuestros modelos producto y categoria porque 
#seran implementados por admin, no un formulario de usuario

#le agregamos al modelo para que se pueda leer los campos de solo lectura
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)

