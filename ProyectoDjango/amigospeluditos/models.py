import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre_de_usuario, email, rut, password=None, **extra_fields):
        if not nombre_de_usuario:
            raise ValueError('El usuario debe tener un nombre de usuario')
        if not email:
            raise ValueError('El usuario debe tener un email')
        if not rut:
            raise ValueError('El usuario debe tener un RUT')
        
        user = self.model(
            nombre_de_usuario=nombre_de_usuario,
            email=self.normalize_email(email),
            rut=rut,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nombre_de_usuario, email, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nombre_de_usuario, email, rut, password, **extra_fields)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nombre_de_usuario = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    celular = models.CharField(max_length=9)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True, max_length=100)
    genero = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombre_de_usuario'
    REQUIRED_FIELDS = ['email', 'rut']

    def __str__(self):
        return self.nombre_de_usuario

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    codigo_sku = models.CharField(primary_key = True, max_length = 10)
    descripcion = models.CharField(max_length = 50)
    precio = models.IntegerField(blank = True, null = True, verbose_name = "Precio")
    disponibilidad = models.CharField(max_length = 10)
    acerca_de = models.CharField(max_length = 100)
    imagen = models.ImageField(upload_to = "imagenes", null = True, blank = True, verbose_name = "Imagen")
    categoria = models.CharField(max_length=10)

    def __str__(self):
        return self.codigo_sku
 
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key = True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank = False, null = False, default = datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)
    
class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank = True, on_delete = models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key = True)
    id_producto = models.ForeignKey('Producto', on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)