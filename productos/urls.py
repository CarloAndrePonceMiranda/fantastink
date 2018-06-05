from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    PerfilList,
    PerfilDetail,
    PerfilCreation,
    PerfilUpdate,
    PerfilDelete,
    ModeloList,
    ModeloDetail,
    ModeloCreation,
    ModeloUpdate,
    ModeloDelete
)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    ###################### Urls Perfiles ######################
    url(r'^PerfilList/$', PerfilList,name='list_perfil'),
    url(r'^Perfil/(?P<pk>[0-9]+)/$', views.PerfilDetail, name='detail_perfil'),
    url(r'^Perfil/nuevo',views.perfil,name="perfil"),
    url(r'^editar_perfil/(?P<pk>\d+)', login_required(PerfilUpdate.as_view()), name='edit_perfil'),
    url(r'^borrar_perfil/(?P<pk>\d+)', login_required(PerfilDelete.as_view()), name='delete_perfil'),
    ###################### Urls Modelos ######################
    url(r'^ModeloList/$', ModeloList,name='list_modelo'),
    url(r'^Modelo/(?P<pk>\d+)', login_required(ModeloDetail.as_view()), name='detail_modelo'),
    url(r'^Modelo/nuevo',views.modelo,name="modelo"),
    url(r'^editar_modelo/(?P<pk>\d+)', login_required(ModeloUpdate.as_view()), name='edit_modelo'),
    url(r'^borrar_modelo/(?P<pk>\d+)', login_required(ModeloDelete.as_view()), name='delete_modelo'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
