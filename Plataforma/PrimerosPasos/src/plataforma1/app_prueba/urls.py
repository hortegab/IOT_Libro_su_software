from django.urls import path
from app_prueba import views
from .apiviews import AlbumAPI

app_name="app_prueba"

urlpatterns = [
    path('info_cacao', views.info_cacao, name="info-cacao"), #actividad 3
    path('info_cacao2', views.info_cacao_form, name="info-cacao2"), #actividad 4
    path('cargar-video', views.showvideo, name="mostrar-video"), #actividad 8

    path('control-manual', views.control_manual, name="control-manual"), #actividad 6
    path('album-imagenes', AlbumAPI.as_view()), #actividad 6
]
