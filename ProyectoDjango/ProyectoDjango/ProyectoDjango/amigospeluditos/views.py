from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def galeria_de_fotos(request):
    return render(request, 'galeria_de_fotos.html')

def inicio_sesion(request):
    return render(request, 'iniciosesion.html')

def registrarse(request):
    return render(request, 'crearcuenta.html')

def royalcanin(request):
    return render(request, 'royalcanin.html')

def correaflexi(request):
    return render(request, 'correaflexi.html')

def nexgard(request):
    return render(request, 'NexGard.html')

def correapepolli(request):
    return render(request, 'correapepolli.html')

def belcando(request):
    return render(request, 'belcando.html')

def americalitter(request):
    return render(request, 'americalitter.html')