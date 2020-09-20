from django.db import models
from datetime import datetime
from core.erp.choices import  gender_choices

# Create your models here.

class TipoEmpleado(models.Model):

    tiṕo_empleado=models.CharField(max_length=100, verbose_name='Tipo Empleado')

    def __str__(self):
        return self.tiṕo_empleado

    class Meta:
        verbose_name='Tipo Empelado'
        verbose_name_plural='Tipo Empleado'
        ordering=['id']


class Categoria(models.Model):
    nombre=models.CharField(max_length=150,verbose_name='Categoria')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        db_table='Categoria'
        ordering=['id']


class Empleado(models.Model):
    categoria=models.ManyToManyField(Categoria)
    tipo_empleado=models.ForeignKey(TipoEmpleado,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=120,verbose_name='Nombre')
    dni= models.CharField(max_length=10, unique=True, verbose_name='Dni')
    fecha_registo = models.DateField(default=datetime.now,verbose_name='fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    edad = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
    cv = models.FileField(upload_to='cv/%Y/%m/%d')


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empelado'
        ordering = ['id']

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombres')
    Apellido = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    cumpleaneos = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    direccion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table= 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.nombre

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.nombre

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']









####################################################################################################################




