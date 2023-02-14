from django.db import models
from django.contrib.auth.models import User


class Usuario( User ):
        
    nome = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    contato = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
