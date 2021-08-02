from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+[
    #path('', views.home, name='home'),
    path('api/auth/', views.CustomAuthToken.as_view()),
    url(r'^perfiles$', views.PerfilesList.as_view()),
    url(r'^perfiles/(?P<pk>[0-9]+)$', views.PerfilesDetail.as_view()),
    url(r'^comentarios$', views.ComentariosList.as_view()),
    url(r'^comentarios/(?P<articulo>[0-9]+)$', views.ComentariosDetail.as_view()),
    url(r'^categorias$', views.CategoriasList.as_view()),
    url(r'^categorias/(?P<pk>[0-9]+)$', views.CategoriasDetail.as_view()),
    url(r'^user$', views.UsuarioList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$', views.UsuarioDetail.as_view()),
    url(r'^articulos$', views.ArticulosList.as_view()),
    url(r'^articulos/(?P<pk>[0-9]+)$', views.ArticulosDetail.as_view()),
    url(r'', views.home.as_view()),
]