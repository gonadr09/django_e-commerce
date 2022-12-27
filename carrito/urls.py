from django.urls import path
from . import views

app_name="carrito"

urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('vaciar/', views.vaciar_carrito, name='vaciar'),
]
