from django.contrib.auth.forms import UserCreationForm
from accounts.models import Usuario

class RegistroUsuarioForm( UserCreationForm ):
    class Meta:
        model = Usuario
        fields = ["nome", "email", "username", "contato", "password1", "password2"]