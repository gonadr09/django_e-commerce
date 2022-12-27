from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriasProducto'

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField()
    stock = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'