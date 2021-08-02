from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('cuentas.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('', include('public.urls')),
    url(r'^', include('cuentas.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)