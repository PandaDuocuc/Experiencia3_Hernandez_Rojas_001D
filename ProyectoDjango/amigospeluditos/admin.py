from django.contrib import admin
from .models import Usuario, Producto, detalle_boleta, Boleta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)