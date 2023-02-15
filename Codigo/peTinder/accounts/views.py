from django.shortcuts import render, redirect
from accounts.forms import RegistroUsuarioForm

def registrar(request):

    form = RegistroUsuarioForm

    if request.method == 'POST': 

        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")

    context = {
        'form': form
    }

    return render(request, 'registration/registrar.html',context=context)