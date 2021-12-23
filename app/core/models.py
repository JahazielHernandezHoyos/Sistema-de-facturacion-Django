from django.db import models
from datetime import *

# Create your models here.

class Employee(models.Model):
    names = models.CharField(max_length=100, verbose_name='Nombres')
    ci = models.CharField(max_length=10, unique=True, verbose_name='Cedula de Identidad')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0,verbose_name='Edad')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Salario')
    state = models.BooleanField(default=True)
    avatar = models.ImageField(max_length=100, upload_to='avatars/', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
        db_table= "empleados"