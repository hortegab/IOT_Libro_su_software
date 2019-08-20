from django import forms
from .models import Produccion_municipios
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("name", "videofile")

class DepartamentosForm(forms.Form):
    departamento = forms.CharField(max_length=50)

class Produccion_municipiosForm(forms.ModelForm):
    class Meta:
        model = Produccion_municipios
        fields = ('departamento',)

