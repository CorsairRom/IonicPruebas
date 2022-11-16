from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class cliente(models.Model):
    rut_cliente = models.CharField(unique=True, max_length = 10, primary_key=True, verbose_name='Rut')
    username = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank = True)
    direccion_cli = models.CharField( max_length = 50, verbose_name='Direccion Principal')
    nombre = models.CharField(max_length = 30)
    apellido_pa = models.CharField(max_length = 30, verbose_name='Apellido Paterno')
    apellido_ma = models.CharField(max_length = 30, verbose_name='Apellido Materno')
    
    def __str__(self):
        return self.rut_cliente
    
class direccion(models.Model):
    nombre_dir = models.CharField(max_length = 50, verbose_name='Nombre direcion')
    descripcion = models.TextField()
    cliente_dir = models.ForeignKey(cliente, on_delete = models.CASCADE, null = True, blank = True, verbose_name='Direccion cliente')
    def __str__(self):
        return self.nombre_dir
    
class usuarioPrueba(models.Model):
    rut = models.CharField(max_length = 50)
    id_tipo_usuario = models.IntegerField()
    
    def __str__(self):
        return self.rut
    
class local(models.Model):
    nombre_local = models.CharField(max_length=50, unique= True, null=True, verbose_name='nombre')
    direccion_local = models.CharField(max_length=200, null=True, verbose_name='direccion')
    
    def __str__(self):
        return self.nombre_local
    
class promocion(models.Model):
    id_local = models.ForeignKey(local, on_delete=models.CASCADE)
    descripcion_promo = models.CharField(max_length=50, null=True, verbose_name='Descripcion')
    nombre_promo = models.CharField(max_length=50 , null=True, verbose_name='nombre')
    fecha_ini = models.DateField(auto_now_add=False, null=True, verbose_name='fecha inicio')
    fecha_fin = models.DateField(auto_now_add=False, null=True, verbose_name='fecha fin')
    
    def __str__(self):
        return self.nombre_promo
