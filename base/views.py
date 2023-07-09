from django.shortcuts import render
from contacto.forms import ContactoForm
from django.core.mail import send_mail
from core import settings

def inicio(request):
    
    form = ContactoForm()
    
    #mostramos inicio con form contacto
    if request.method == 'GET':
        return render(request, 'inicio.html', {
            'form':form
        })
        
    #recibimos el form
    elif request.method == 'POST':
        form_request = ContactoForm(request.POST)
        
        if form_request.is_valid():
            email = form_request.cleaned_data['email']
            asunto = form_request.cleaned_data['asunto']
            mensaje = form_request.cleaned_data['mensaje']
            
            mensaje = f"Email de: {email} \nMensaje: {mensaje}"
            print(mensaje)
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