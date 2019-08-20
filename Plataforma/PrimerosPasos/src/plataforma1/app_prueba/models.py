from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.IntegerField()

    def __str__(self):
        return self.nombre

class ProduccionCacao(models.Model):
    cod_dep = models.IntegerField()
    departamento = models.CharField(max_length=50)
    cod_mun = models.IntegerField()
    municipio = models.CharField(max_length=50)
    grupo_cultivo = models.CharField(max_length=50)
    sub_grupo_cultivo = models.CharField(max_length=50)
    cultivo = models.CharField(max_length=50)
    sistema_productivo = models.CharField(max_length=50)
    codigo_cultivo = models.IntegerField()
    nombre_cientifico = models.CharField(max_length=50)
    periodo = models.IntegerField()
    area_sembrada = models.FloatField() #ha
    area_cosechada = models.FloatField() #ha
    produccion = models.FloatField() # ton
    rendimiento = models.FloatField() #ton/ha
    estado_produccion = models.CharField(max_length=50)


    def __str__(self):
        return self.municipio+" "+ str(self.produccion)+ "ton"

class Departamentos(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Produccion_municipios(models.Model):
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    cod_municipio = models.IntegerField()
    municipio = models.CharField(max_length=50)
    cultivo = models.CharField(max_length=50)
    codigo_cultivo = models.IntegerField()
    nombre_cientifico = models.CharField(max_length=50)
    periodo = models.IntegerField()
    area_sembrada = models.FloatField()
    area_cosechada = models.FloatField()
    produccion = models.FloatField()
    rendimiento = models.FloatField()
    estado_produccion = models.CharField(max_length=50)

    def __str__(self):
        return self.municipio


class AlbumImagenes(models.Model):
    """ esta tabla se encarga de registrar todas las imagenes del cielo tomadas """
    imagen = models.ImageField(upload_to='album/imagenes', height_field=None, width_field=None, max_length=None)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.imagen

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'AlbumImagenes'
        verbose_name_plural = 'AlbumImageness'

class Video(models.Model):
    name = models.CharField(max_length=50)
    videofile = models.FileField(upload_to='videos/', null = True, max_length=100, verbose_name="")

    def __str__(self):
        return self.name +" : "+ str(self.videofile)