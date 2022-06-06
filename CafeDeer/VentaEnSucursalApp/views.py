from django.shortcuts import render, HttpResponse

# Create your views here.

def ofrecerProductos(request):

    return render(request, "VentaEnSucursalApp/ofrecerProductos.html")

def solicitarPago(request):

    return render(request, "VentaEnSucursalApp/solicitarPago.html")

def entregarPedido(request):

    return render(request, "VentaEnSucursalApp/entregarPedido.html")

def hacerCorteDeCaja(request):

    return render(request, "VentaEnSucursalApp/hacerCorteDeCaja.html")
