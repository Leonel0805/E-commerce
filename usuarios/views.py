from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


#REGISTRO
def registro(request):

    #creamos el formulario registro
    form = UserCreationForm()
    if request.method == 'GET':
        return render(request, 'registro.html',{
            'form':form
        })
    
    #recibimos el formulario y validamos
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        #validamos
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('productos:productos')
        
        else:
            error = 'Error al validar los datos'
            return render(request, 'registro.html',{
                'form':form,
                'error':error
            })
        
#LOGIN
def inicio_sesion(request):
    
    form = AuthenticationForm()
    
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html',{
            'form':form
        })
        
    if request.method == 'POST':
        #autenticamos
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password )
        
        #SI recibimos un usuario valido
        if user is not None:
            login(request, user)
            return redirect('productos:productos')
        
        else:
            return render(request, 'inicio_sesion.html',{
            'form':form,
            'error': 'Error al iniciar sesion'
        })
            
#CERRAR SESION
def cerrar_sesion(request):
    
    logout(request)
    return redirect('usuarios:registro')