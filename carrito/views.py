from django.shortcuts import redirect
from .carrito import Carrito
from tienda.models import Producto
from django.http import JsonResponse
import json

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregarProducto(producto)
    return redirect("tienda")
    print(carrito)
    carrito1 = json.dumps(carrito.carrito)
    print(carrito1)
    return JsonResponse(carrito1)

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminarProducto(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restarProducto(producto)
    return redirect("tienda")

def vaciar_carrito(request):
    carrito = Carrito(request)
    carrito.vaciarCarrito()
    return redirect("tienda")