from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/animal/registrar-animal/
    path('registrar/', views.registrar, name='registrarAnimal'),
    path('detalhar/<int:id>/', views.detalharPerfilAnimal, name='detalharAnimal'),
]

