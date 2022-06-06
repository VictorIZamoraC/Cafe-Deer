from django.urls import path
from VentaEnSucursalApp import views

urlpatterns = [
    path('', views.ofrecerProductos, name="Ofrecer Productos"),
    path('solicitarPago/', views.solicitarPago, name="Solicitar Pago"),
    path('entregarPedido/', views.entregarPedido, name="Entregar Pedido"),
    path('hacerCorteDeCaja/', views.hacerCorteDeCaja, name="Hacer Corte De Caja"),
]