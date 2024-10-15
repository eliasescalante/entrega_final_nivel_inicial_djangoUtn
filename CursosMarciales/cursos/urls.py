from django.urls import path, include
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:curso_id>/', views.course_detail, name='course_detail'),
    path('crear/', views.course_create, name='course_create'),
    path('editar/<int:pk>/', views.course_update, name='course_update'),
    path('eliminar/<int:pk>/', views.course_delete, name='course_delete'),
    path('usuarios/', include(('users.urls', 'users'), namespace='users')),
]
