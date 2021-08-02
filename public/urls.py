from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from public import views

urlpatterns = [
    path('data/Morbilidad_Adolescente',views.DataMorbilidadView.as_view()),
    path('data/Riesgo_Adolescente',views.DataRiesgoView.as_view()),
    path('data/Tamizaje_Adolescente',views.DataTamizajeView.as_view()),
    path('data',views.DataAdolescentes.as_view()),
    path('mapas',views.DataMapas.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)