from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Perfil, Modelo
from .forms import PerfilForm, ModeloForm
import pprint
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
############################################Views Perfil########################
class PerfilList(ListView):
    model = Perfil
    fields = ['id', 'modelo', 'material','descripcion','precio']
class PerfilDetail(DetailView):
    model = Perfil
    fields = ['id', 'perfil','nombre', 'material','descripcion','precio','activo','imagen']
class PerfilCreation(CreateView):
    model = Perfil
    success_url = reverse_lazy('productos:list_perfil')
    fields = ['perfil', 'material','descripcion','precio','metraje','desperdicio','activo','imagen']
class PerfilUpdate(UpdateView):
    model = Perfil
    success_url = reverse_lazy('productos:list_perfil')
    fields = ['perfil','nombre', 'material','descripcion','precio','metraje','desperdicio','activo','imagen']
class PerfilDelete(DeleteView):
    model = Perfil
    success_url = reverse_lazy('productos:list_perfil')

def principal(request):
    perfil = Perfil.objects.order_by('id')
    template = loader.get_template('home.html')
    context = {
        'perfil': perfil
    }
    return HttpResponse(template.render(context, request))

def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save()
            perfil.save()
            return HttpResponseRedirect('/PerfilList')
    else:
        form = PerfilForm()
    template = loader.get_template('productos/nuevo.html')
    context = {
        'form': form
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/PerfilList/')

def PerfilList(request):
    queryset = Perfil.objects.all().order_by('perfil')
    context = {
        'queryset':queryset
    }
    return render(request, "productos/perfil_list.html",context)

def PerfilDetail(request,pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    modelos = Modelo.objects.filter(perfil=pk)
    template = loader.get_template('productos/perfil_detail.html')
    context = {
        'perfil': perfil,
        'modelos': modelos
        }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/PerfilList/')

############################################Views Modelos#######################

class ModeloList(ListView):
    model = Modelo
    fields = ['id', 'nombre', 'descripcion','imagen','perfil','activo']
class ModeloDetail(DetailView):
    model = Modelo
    fields = ['id', 'nombre', 'descripcion','imagen','perfil','activo']
class ModeloCreation(CreateView):
    model = Modelo
    success_url = reverse_lazy('productos:list_modelo')
    fields = ['id', 'nombre', 'descripcion','imagen','perfil','activo']
class ModeloUpdate(UpdateView):
    model = Modelo
    success_url = reverse_lazy('productos:list_modelo')
    fields = ['id', 'nombre', 'descripcion','imagen','perfil','activo']
class ModeloDelete(DeleteView):
    model = Modelo
    success_url = reverse_lazy('productos:list_modelo')

def principal(request):
    modelo = Modelo.objects.order_by('id')
    template = loader.get_template('home.html')
    context = {
        'modelo': modelo
    }
    return HttpResponse(template.render(context, request))

def modelo(request):
    queryset = Perfil.objects.order_by('perfil')
    if request.method == 'POST':
        form = ModeloForm(request.POST, request.FILES)
        if form.is_valid():
            modelo = form.save()
            modelo.save()
            return HttpResponseRedirect('/PerfilList/')
    else:
        form = ModeloForm()
    template = loader.get_template('productos/nuevo_modelo.html')
    context = {
        'form': form,
        'queryset':queryset
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/ModeloList/')

def ModeloList(request):
    queryset = Modelo.objects.all().order_by('id').reverse()
    count = Modelo.objects.count()
    context = {
        'queryset':queryset,
        'count':count
    }
    return render(request, "productos/modelo_list.html",context)
