from django.shortcuts import render

# Create your views here.
def consulta_datos_piscicultura(request):
    return render(request, "piscicultura/consumo_datos.html", {})