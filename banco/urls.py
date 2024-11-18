from django.urls import path
from . import views

urlpatterns = [
    path('api/registrar/', views.registrar_transaccion, name='registrar_transaccion'),
    path('api/consultar/<str:referencia>/', views.consultar_transaccion, name='consultar_transaccion'),
]
