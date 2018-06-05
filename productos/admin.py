from django.contrib import admin
from .models import Modelo, Perfil
# Register your models here.
class ModeloAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','imagen']
    class Meta:
        model = Modelo

admin.site.register(Modelo, ModeloAdmin)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    class Meta:
        model = Perfil

admin.site.register(Perfil, PerfilAdmin)
