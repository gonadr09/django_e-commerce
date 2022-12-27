from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

class VistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {'form':form})

    def set(request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #usuario = form.save()  # se guarda en la base de datos
            form.save()  # se guarda en la base de datos
            #login(request, usuario)
            return redirect("inicio")
        else:
            for message in form.error_messages:
                messages.error(request, form.error_messages[message])
            return render(request, "registro/registro.html", {'form':form})