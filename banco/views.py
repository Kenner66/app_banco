from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UsuarioBanco, Transaccion
import uuid

@api_view(['POST'])
def registrar_transaccion(request):
    """
    Endpoint para registrar una nueva transacción.
    """
    data = request.data
    identificacion = data.get('identificacion')
    monto = data.get('monto')
    concepto = data.get('concepto')

    # Validación de datos
    if not identificacion or not monto or not concepto:
        return Response({"error": "Datos incompletos"}, status=400)

    try:
        usuario = UsuarioBanco.objects.get(identificacion=identificacion)
    except UsuarioBanco.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=404)

    # Crear la transacción
    referencia = str(uuid.uuid4())[:8]  # Generar un identificador único
    transaccion = Transaccion.objects.create(
        usuario=usuario,
        referencia=referencia,
        monto=monto,
        concepto=concepto,
        estado='Pendiente'
    )

    return Response({
        "mensaje": "Transacción registrada exitosamente",
        "referencia": transaccion.referencia,
        "estado": transaccion.estado
    })


@api_view(['GET'])
def consultar_transaccion(request, referencia):
    """
    Endpoint para consultar el estado de una transacción por su referencia.
    """
    try:
        transaccion = Transaccion.objects.get(referencia=referencia)
        return Response({
            "referencia": transaccion.referencia,
            "estado": transaccion.estado,
            "monto": transaccion.monto,
            "concepto": transaccion.concepto,
            "usuario": transaccion.usuario.nombre,
            "fecha_creacion": transaccion.fecha_creacion,
            "fecha_actualizacion": transaccion.fecha_actualizacion,
        })
    except Transaccion.DoesNotExist:
        return Response({"error": "Transacción no encontrada"}, status=404)
