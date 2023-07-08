from django.shortcuts import render, redirect
from carrito.carrito import Carro
from productos.models import Producto 

def tienda(request):
    
    productos = Producto.objects.all()
    carro = Carro(request)
    total = carro.obtener_total()
    if request.method == 'GET':

        return render(request, 'tienda.html',{
            'productos':productos,
            # le pasamos total a tienda y como widget esta incluido lo puede usar
            'total':total
        })
        
def agregar_producto(request, producto_id):
    
    carro = Carro(request)
    producto = Producto.objects.get(pk=producto_id)
    carro.agregar_producto(producto)        
    return redirect('tienda:tienda')


def restar_producto(request, producto_id):
    
    carro = Carro(request)
    producto = Producto.objects.get(pk=producto_id)
    carro.restar_producto(producto)        
    return redirect('tienda:tienda')
