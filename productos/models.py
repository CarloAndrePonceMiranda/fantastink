from django.db import models
import random
import os

# Create your models here.
def get_filename_ext(filepath):
    nombre_base = os.path.basename(filepath)
    nombre, ext = os.path.splitext(nombre_base)
    return nombre, ext


def upload_image_path(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "productos/modelo/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )
            
def upload_image_pathv(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "productos/perfil/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

class Perfil(models.Model):
    perfil = models.IntegerField(blank=False)
    nombre = models.CharField(max_length=50,blank=False,null=True)
    descripcion = models.CharField(max_length=255,blank=True,null=True,default='Sin descripción')
    metraje = models.DecimalField(max_digits=10,decimal_places=3,blank=False)
    desperdicio = models.DecimalField(max_digits=10,decimal_places=3,blank=False)
    precio = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    material = models.CharField(max_length=255,blank=False)
    activo = models.BooleanField(blank=False,default=True)
    imagen = models.ImageField(upload_to=upload_image_pathv, null=True, blank=True)
    def __str__(self):
        return self.nombre



class Modelo(models.Model):
    imagen = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    perfil = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)
    activo = models.BooleanField(blank=False,default=True)
    def __str__(self):
        return self.nombre
