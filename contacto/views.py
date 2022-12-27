from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        formulario  = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            send_mail('Nuevo mensaje de formulario', nombre + ' ha enviado un mensaje: \n' + contenido, email, ['myemail@mail.com'])
            return redirect("/contacto/?valido")
    else:
        formulario = FormularioContacto()
    return render(request, 'contacto/contacto.html', {'formulario': formulario})


