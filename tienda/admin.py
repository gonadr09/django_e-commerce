from django.contrib import admin
from .models import Producto, CategoriaProducto

# Register your models here.

class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
