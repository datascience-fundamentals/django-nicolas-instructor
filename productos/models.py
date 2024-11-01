from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return str(self.nombre)

# CASCADE: elimina los productos asociados a la categoria
# PROTECT: lanza un error al intentar eliminar una categoria
# RESTRICT: eliminar solo los productos que no tiene categoria
# SET_NULL: asgina el valor NULL a la columna categoria de aquellos productos que le pertenecian
# SET_DEFAULT: asigna el valor por defecto establecido para la columna categoria de aquellos productos que le pertenecian


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.nombre)
