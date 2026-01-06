from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('inicio.urls')),
    path('admin/', admin.site.urls),
    path("operador/", include('operadores.urls')),
    path("equipamento/", include(("equipamentos.urls", "equipamentos"), namespace="equipamentos")),
    path('plataforma/', include('plataforma.urls')),
]
    