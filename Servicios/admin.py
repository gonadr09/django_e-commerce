from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # solo lectura
    list_display = ("titulo",) # mostrar columnas en panel de admin

admin.site.register(Servicio, ServicioAdmin)
