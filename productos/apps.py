from django.apps import AppConfig
from .models import Modelo

class ModeloAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    class Meta:
        model = Modelo

admin.site.register(Modelo, ModeloAdmin)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    class Meta:
        model = Perfil

admin.site.register(Perfil, PerfilAdmin)
