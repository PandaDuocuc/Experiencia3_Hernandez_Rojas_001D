from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre     = models.CharField(max_length = 20)
    apellidos  = models.CharField(max_length = 20)
    celular    = models.CharField(max_length = 9)
    rut        = models.CharField(primary_key = True, max_length = 12)
    email      = models.EmailField(unique = True, max_length = 100, blank = True, null = True)
    genero     = models.CharField(max_length = 10)
    contraseña = models.CharField(max_length = 20)
    activo     = models.IntegerField()