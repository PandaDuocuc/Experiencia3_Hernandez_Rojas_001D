from django.shortcuts import render, redirect
from .forms import UsuarioForm, ProductoForm
from .models import Usuario, Producto, Boleta, detalle_boleta
from amigospeluditos.compra import Carrito
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def galeria_de_fotos(request):
    return render(request, 'galeria_de_fotos.html')

def inicio_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'iniciosesion.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'iniciosesion.html', {'form': form})

def registrarse(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("nombre_de_usuario")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'crearcuenta.html', {'form': form})
    else:
        form = UsuarioForm()
    return render(request, 'crearcuenta.html', {'form': form})

def royalcanin(request):
    return render(request, 'royalcanin.html')

def correaflexi(request):
    return render(request, 'correaflexi.html')

def nexgard(request):
    return render(request, 'nexgard.html')

def correapepolli(request):
    return render(request, 'correapepolli.html')

def belcando(request):
    return render(request, 'belcando.html')

def americalitter(request):
    return render(request, 'americalitter.html')

@login_required
def producto(request):
    productito = Producto.objects.raw('Select * from amigospeluditos_producto')
    datos={
        'producto': productito
    }
    return render(request, 'producto.html', datos)

@login_required
def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    return render(request, 'crear.html', {'form': form})

@login_required
def modificar(request, id):
    productoModificado = Producto.objects.get(codigo_sku = id) #buscamos el objeto
    datos ={
        'form': ProductoForm(instance = productoModificado)
    }
    if request.method == "POST":
        formulario = ProductoForm(data = request.POST, instance = productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect ('producto')
    return render(request, 'modificar.html', datos)

@login_required
def eliminar(request, id): 
    productoEliminado = Producto.objects.get(codigo_sku = id) #similar a select * from... where...
    productoEliminado.delete()
    return redirect ('producto')

def mostrar(request):
    productito = Producto.objects.all()
    datos={
        'producto': productito
    }
    return render(request, 'mostrar.html', datos)

@login_required
def tienda(request):
    productito = Producto.objects.all()
    datos={
        'producto': productito
    }
    return render(request, 'tienda.html', datos)

def agregar_producto(request,id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo_sku = id)
    carrito_compra.agregar(producto = producto)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo_sku = id)
    carrito_compra.eliminar(producto = producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo_sku = id)
    carrito_compra.restar(producto = producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')

@login_required
def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(codigo_sku = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)

@login_required
def cierre_sesion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')  # Redirige a la página principal después de cerrar sesión
    return render(request, 'cierresesion.html')

def perfil(request):
    return render(request, 'perfil.html')