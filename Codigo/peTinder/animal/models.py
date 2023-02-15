from django.db import models
from accounts.models import Usuario

# Create your models here.
class Animal( models.Model ):

    SEXO_ESCOLHAS = {
        ("M", "Masculino"),
        ("F", "Feminino")
    }
        
    nome = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    idade = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )


    sexo = models.CharField(
        max_length=1, 
        choices= SEXO_ESCOLHAS,
        blank=False,
        null=False,
    )

    cor = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        help_text="Coloração do seu animal"
    )

    raca = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        help_text="Raça do seu animal"
    )

    comportamento = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )

    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    foto = models.ImageField(null=True, blank=True ,upload_to='images/')


