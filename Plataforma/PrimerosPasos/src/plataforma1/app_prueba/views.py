from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiantes, ProduccionCacao, Produccion_municipios, AlbumImagenes, Video
from .forms import DepartamentosForm, Produccion_municipiosForm, VideoForm


def showvideo(request):
    try:
        lastvideo = Video.objects.last()
        videofile = lastvideo.videofile
        if request.POST:
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        context = {"videofile": videofile, "form": form}
    except:
        form = VideoForm()
        context = {"form": form}
        if request.POST:
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, "app_prueba/videos.html", context)
    return render(request, "app_prueba/videos.html", context)

# Create your views here.
def index(request):
    integrantes = Estudiantes.objects.all()
    integrantes = integrantes.values("nombre", "cedula")
    print(integrantes)
    return HttpResponse(integrantes)

def index1(request):
    return render(request, "app_prueba/index.html")

def info_cacao(request):
    departamento = "SANTANDER"
    cacao = ProduccionCacao.objects.filter(departamento=departamento).order_by("municipio")
    cacao = cacao.values("area_sembrada", "area_cosechada", "produccion", "rendimiento", "municipio")
    total_area = 0
    total_produccion = 0
    for dat in cacao:
        total_area=total_area+dat["area_sembrada"]
        total_produccion  = total_produccion + dat["produccion"]

    respuesta = {"cacao": cacao, "area_total": total_area,
                "total_produccion": total_produccion, 
                "departamento": departamento,}

    return render(request, "app_prueba/info_cacao.html", respuesta)

def info_cacao_form(request):
    form_dep = Produccion_municipiosForm()
    if request.POST:
        print(request.POST)
        cacao = Produccion_municipios.objects.filter(departamento_id = request.POST["departamento"]).order_by("municipio")
        cacao = cacao.values("area_sembrada", "area_cosechada", "produccion", "rendimiento", "municipio")
        respuesta = {"cacao": cacao,"form_dep": form_dep}
    else:
        respuesta = {"form_dep": form_dep}
    return render(request, "app_prueba/info_cacao2.html", respuesta)
    

def control_manual(request):
    album = AlbumImagenes.objects.all()
    respuesta = {"imagenes": album,}
                
    return render(request, "app_prueba/control_manual.html", respuesta)


