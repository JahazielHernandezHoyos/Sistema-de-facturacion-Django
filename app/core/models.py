from django.db import models
from datetime import *

# Create your models here.
class type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']

class Employee(models.Model):
    categ = models.ManyToManyField(Category, verbose_name="Categorias")
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    names = models.CharField(max_length=100, verbose_name='Nombres')
    ci = models.CharField(max_length=10, unique=True, verbose_name='Cedula de Identidad')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0,verbose_name='Edad')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Salario')
    state = models.BooleanField(default=True)
    #gender = models.CharField(max_length=50)
    avatar = models.ImageField(max_length=100, upload_to='avatars/', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
        db_table= "empleados"

