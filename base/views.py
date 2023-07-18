from django.shortcuts import render
from contacto.forms import ContactoForm
from django.core.mail import send_mail
from core import settings
from carrito.carrito import Carro
from pedidos.views import email_pedido
from productos.models import Producto

def inicio(request):
    
    # Formulario de Contacto
    form = ContactoForm()
    
    # Obtenemos todos los productos con oferta
    productos = Producto.objects.filter(oferta=True)
    
    # Iniciamos pagina
    if request.method == 'GET':
        return render(request, 'inicio.html', {
            'form':form,
            'productos':productos
        })
        
    #recibimos el form
    elif request.method == 'POST':
        form_request = ContactoForm(request.POST)
        
        if form_request.is_valid():
            email = form_request.cleaned_data['email']
            asunto = form_request.cleaned_data['asunto']
            mensaje = form_request.cleaned_data['mensaje']
            
            mensaje = f"Email de: {email} \nMensaje: {mensaje}"
            
            send_mail(
                subject=asunto,
                message=mensaje,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['leoulirodriguez@gmail.com'],
                fail_silently=False,
            )
            
            return render(request, 'inicio.html',{
                'mensaje':"Correo enviado correctamente!",
                'form':form
            })
            
def finalizar_compra(request):
    form = ContactoForm()
    carro = Carro(request)
    
    if request.method == 'GET':
                
        #enviamos un mail con todo lo que tiene a una direccion de email
        email_pedido(request)
        
        #vaciamos carrito despues de enviar los datos con el request
        carro.vaciar_carrito()

        return render(request, 'inicio.html',{
            'mensaje':"Gracias por su compra",
            'form':form
        })