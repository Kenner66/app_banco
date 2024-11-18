from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UsuarioBanco, Transaccion

@admin.register(UsuarioBanco)
class UsuarioBancoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'identificacion', 'fecha_creacion')

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'usuario', 'monto', 'concepto', 'estado', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('referencia', 'usuario__nombre', 'concepto')

