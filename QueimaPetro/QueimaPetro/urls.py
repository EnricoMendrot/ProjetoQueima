from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("operadores/", include('operadores.urls')),
    path("equipamentos/", include(("equipamentos.urls", "equipamentos"), namespace="equipamentos")),
    path('plataforma/', include('plataforma.urls')),
]
    