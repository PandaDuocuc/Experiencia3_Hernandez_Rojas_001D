from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name = "index"),
    path('index/quienes-somos', views.quienes_somos, name = "quienes-somos"),
    path('index/galeria-de-fotos', views.galeria_de_fotos, name = "galeria-de-fotos"),
    path('index/inicio-sesion', views.inicio_sesion, name = "inicio-sesion"),
    path('index/registrarse', views.registrarse, name = "registrarse"),
    path('index/royal-canin', views.royalcanin, name = "royal-canin"),
    path('index/correa-flexi', views.correaflexi, name = "correa-flexi"),
    path('index/nexgard', views.nexgard, name = "NexGard"),
    path('index/correa-pepolli', views.correapepolli, name = "correa-pepolli"),
    path('index/belcando', views.belcando, name = "belcando"),
    path('index/americalitter', views.americalitter, name = "americalitter"),
]