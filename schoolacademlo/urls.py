from django.contrib import admin
from django.urls import path, include

from Clase.views import clases_all, clases_by_id
from Estudiante.views import estudiantes_all, estudiantes_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Clase/', include('Clase.urls')),
    ]