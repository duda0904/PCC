from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.models import Usuario
from animal.models import Animal
from animal.forms import RegistroAnimalForm

@login_required
def getUser(request): 
    return Usuario.objects.get(pk=request.user.id)


@login_required
def registrar(request):

    form = RegistroAnimalForm

    if request.method == 'POST': 

        form = RegistroAnimalForm(request.POST)
        
        if form.is_valid():
            novo_animal = form.save(commit=False)
            novo_animal.dono = getUser(request)
            novo_animal.save()
            return redirect("/animal/registrar")

    context = {
        'form': form
    }

    return render(request, 'animal/registrar.html',context=context)


def detalharPerfilAnimal( request, id ):
    animal = Animal.objects.get(pk=id)

    context = {
        "animal" : animal,
        "dono" : animal.dono
    }

    return render(request, 'animal/detalhar.html',context=context)
