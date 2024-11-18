from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
 
#Modelo que representa un usuario en el sistema bancario.
#Este usuario puede ser cualquier cliente (estudiante, profesor, etc.).

class UsuarioBanco(models.Model):
   
    nombre = models.CharField(max_length=100)  # Nombre completo del usuario
    email = models.EmailField(unique=True)  # Email único del usuario
    identificacion = models.CharField(max_length=50, unique=True)  # DNI o identificación única
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de registro en el sistema

    def __str__(self):
        return f"{self.nombre} ({self.identificacion})"


#   Modelo que representa una transacción bancaria.
class Transaccion(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]

    usuario = models.ForeignKey(UsuarioBanco, on_delete=models.CASCADE)  # Relación con UsuarioBanco
    referencia = models.CharField(max_length=100, unique=True)  # Identificador único para la transacción
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Monto de la transacción
    concepto = models.CharField(max_length=200)  # Concepto del pago (ej. Matrícula, Mensualidad)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')  # Estado de la transacción
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó la transacción
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Fecha en que se actualizó por última vez el estado

    def __str__(self):
        return f"Transacción {self.referencia} - {self.estado}"
