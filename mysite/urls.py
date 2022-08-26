from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('operaciones/', include('operaciones.urls')),
    path('polls/', include('encuesta.urls')),
    path('admin/', admin.site.urls),
]
