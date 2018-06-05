# This Python file uses the following encoding: utf-8
from django import forms
from .models import Perfil, Modelo
from django.forms import Textarea,TextInput,NumberInput,FileInput,Select
choicestxt=(('Madera','Madera'),('Poliestireno','Poliestireno'))
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        labels = {
            'perfil': 'Perfil',
            'nombre': 'Nombre',
            'descripcion' :	'Descripción',
            'metraje' :	'Metraje (m)',
            'desperdicio' :	'Desperdicio (cm)',
            'material' :	'Material',
            'precio' :	'Precio',
            'activo' :	'¿Activo?',
            }
        widgets = {
                        'nombre': TextInput(attrs={
                                                'class':'form-control',
                                                'id': 'nombre',
                                                'name': 'nombre',
                                                'placeholder':'Nombre(s)'
                                                }),
                        'descripcion': Textarea(attrs = {
                                                'id': 'descripcion',
                                                'class':'form-control',
                                                'cols':'40',
                                                'rows':'4',
                                                'placeholder':'Descripción'
                                                }),
                        'material': forms.Select(attrs={
                                                'id': 'material',
                                                'data-init-plugin': 'cs-select',
                                                'class':'cs-select cs-skin-slide',
                                                'name': 'material',
                                                },
                                                choices=choicestxt),
                        'perfil': TextInput(attrs={
                                                'class':'form-control',
                                                'id': 'perfil',
                                                'name': 'perfil',
                                                'placeholder':'Perfil'
                                                }),
                        'metraje': NumberInput(attrs={
                                                'class':'form-control',
                                                'id': 'metraje',
                                                'name': 'metraje',
                                                'placeholder':'0000,00'
                                                }),
                        'desperdicio': NumberInput(attrs={
                                                'class':'form-control',
                                                'id': 'desperdicio',
                                                'name': 'desperdicio',
                                                'placeholder':'0000,00'
                                                }),
                        'precio': NumberInput(attrs={
                                                'class':'form-control',
                                                'id': 'precio',
                                                'name': 'precio',
                                                'placeholder':'0000,00'
                                                }),
                    }

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'descripcion' :	'Descripción',
            'perfil' :	'Perfil (Previamente Registrado)',
            'imagen': 'Imagen (JPG/PNG)'

            }
        widgets = {
                        'nombre': TextInput(attrs={
                                                'class':'form-control',
                                                'id': 'nombre_modelo',
                                                'name': 'nombre_modelo',
                                                'placeholder':'Nombre(s)'
                                                }),
                        'descripcion': TextInput(attrs={
                                                'class':'form-control',
                                                'id': 'descripcion',
                                                'name': 'descripcion',
                                                'placeholder':'Descripción'
                                                }),
                        'perfil': forms.Select(attrs={
                                                'id': 'material',
                                                'name': 'material',
                                                'data-init-plugin': 'cs-select',
                                                'class':'cs-select cs-skin-slide',
                                                }),
                        'imagen': FileInput(attrs = {
                                                'id': 'imagen',
                                                'name': 'imagen',
                                                'class':'form-control-file',
                                                }),
                    }
