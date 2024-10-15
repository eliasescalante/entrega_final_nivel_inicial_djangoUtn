from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Curso
from .forms import CursoForm

def is_admin(user):
    #Para identificar si el usuario logeado es un admin
    return user.is_superuser

@login_required
def course_list(request):
    #Para mostrar la lista de cursos
    cursos = Curso.objects.all()
    return render(request, 'cursos/course_list.html', {'cursos': cursos})

@login_required
def course_detail(request, curso_id):
    #Para mostrar el detalle de un curso
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/course_detail.html', {'curso': curso})

@user_passes_test(is_admin)
def course_create(request):
    #Para crear un curso
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos:course_list')
    else:
        form = CursoForm()
    return render(request, 'cursos/course_form.html', {'form': form})

@user_passes_test(is_admin)
def course_update(request, pk):
    #Para actualizar un curso
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:course_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/course_form.html', {'form': form})

@user_passes_test(is_admin)
def course_delete(request, pk):
    #Para eliminar un curso
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos:course_list')
    return render(request, 'cursos/course_confirm_delete.html', {'curso': curso})


