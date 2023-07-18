from django.shortcuts import render
from carrito.carrito import Carro
from .models import Pedido
from django.core.mail import send_mail
from core import settings

#importamos para renderizar archivo html con jinja
from django.template import engines

def pedido(request):
    
    #le pasamos nuevamente la variable total porque no es global, deberiamos optimizar eso
    #con el contextprocessor
    carro = Carro(request)
    total = carro.obtener_total()
    
    #print(total)
    if request.method == 'GET':
        #creamos nuestro pedido usando Pedido.objects.create para guardarlo en la base de datos
        
        return render(request, 'pedidos.html',{
            'total':total
        })
        
#creamos una funcion que reciba el request y lo usamos en la url de finalizar compra
def email_pedido(request):

    lista = []
    carro = Carro(request)
 
    # Iteramos sobre cada elemento del carro, aunque seria mejor guardar cada valor en un diccionario
    for fruta in carro.carro.items():
       #print(fruta[1]['nombre'])
        fruta_pedido = (fruta[1]['nombre'], fruta[1]['cantidad'])
        lista.append(fruta_pedido)
    
    print('Email enviado')
    total = carro.obtener_total()
    
    #abrimos nuestro html para enviar los datos del pedido realizado
    #with open('pedidos/templates/pedido_email.html', 'r') as archivo:
    
    #    html_message2 = archivo.read()
    html_content = generar_contenido_html(request, lista)
    
    
    #si enviamos un html_message el messge se ignora automaticamente. No se envia al email
    send_mail(
        subject="Compra Finalizada",
        message=f"Gracias por su compra en Verdulería MA: {lista}\nTotal:{total}", #queda ignorado
        html_message= html_content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        fail_silently=False,
    )
    
def generar_contenido_html(request, lista):
  
    html_content = render(request, 'pedido_email.html', {
        'lista':lista
    }).content.decode('utf-8')
    return html_content
