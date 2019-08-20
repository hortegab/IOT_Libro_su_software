from django.urls import path
from piscicultura import views
from .apiviews import TemperaturaAPIPiscicultura, PhAPIPiscicultura, O2DisueltoAPI, \
                      PozoAPI

app_name="piscicultura"

urlpatterns = [
    # url para las API
   path("temperatura-pozo", TemperaturaAPIPiscicultura.as_view()),
   path("ph-pozo", PhAPIPiscicultura.as_view()),
   path("oxigeno-disuelto", O2DisueltoAPI.as_view()),
   path("lista-pozos", PozoAPI.as_view()),   
   # para las  graficas
   path("grafica-datos", views.consulta_datos_piscicultura, name="grafica-datos"),
]

