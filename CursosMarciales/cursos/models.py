from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()
    descripcion = models.TextField()
    profesor = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    cupo = models.IntegerField()

    def __str__(self):
        return str(self.nombre)
