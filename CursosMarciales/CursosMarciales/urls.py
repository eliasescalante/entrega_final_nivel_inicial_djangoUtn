from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('users.urls', namespace='users')),
    path('cursos/', include('cursos.urls', namespace='cursos')),
    path('', RedirectView.as_view(url='/usuarios/login/', permanent=False)),
]