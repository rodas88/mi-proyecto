from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Añade campos adicionales aquí si es necesario
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

