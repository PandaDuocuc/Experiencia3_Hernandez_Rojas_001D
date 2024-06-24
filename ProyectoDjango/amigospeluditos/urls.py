from django.urls import path
from amigospeluditos.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('quienes-somos/', quienes_somos, name = "quienes-somos"),
    path('galeria-de-fotos/', galeria_de_fotos, name = "galeria-de-fotos"),
    path('inicio-sesion/', inicio_sesion, name = "inicio-sesion"),
    path('registrarse/', registrarse, name = "registrarse"),
    path('royal-canin/', royalcanin, name = "royal-canin"),
    path('correa-flexi/', correaflexi, name = "correa-flexi"),
    path('nexgard/', nexgard, name = "nexgard"),
    path('correa-pepolli/', correapepolli, name = "correa-pepolli"),
    path('belcando/', belcando, name = "belcando"),
    path('americalitter/', americalitter, name = "americalitter"),
    path('producto/', producto, name = "producto"),
    path('crear/', crear, name = "crear"),
    path('modificar/<id>', modificar, name = "modificar"),
    path('eliminar/<id>', eliminar, name = 'eliminar'),
    path('mostrar/', mostrar, name = "mostrar"),
    path('restar/<id>', restar_producto, name = "restar"),
    path('limpiar/', limpiar_carrito, name = "limpiar"),
    path('agregar/<id>', agregar_producto, name = "agregar"),
    path('eliminar/<id>', eliminar_producto, name = "eliminar"),
    path('generarBoleta/', generarBoleta, name = "generarBoleta"),
    path('tienda/', tienda, name = "tienda"),
    path('cierre-sesion/', cierre_sesion, name = "cierre-sesion"),
    path('perfil/', perfil, name = "perfil")
]