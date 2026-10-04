from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    class Perfil(models.TextChoices):
        ADMINISTRADOR = "ADMINISTRADOR", "Administrador"
        ATENDENTE = "ATENDENTE", "Atendente"

    email = models.EmailField(
        unique=True
    )

    perfil = models.CharField(
        max_length=20,
        choices=Perfil.choices,
        default=Perfil.ATENDENTE
    )