from django.db import models
from applications.base.models import ClaseModelo
from applications.cli.models import Cliente
from applications.dom.models import Domicilio
from applications.prod.models import Etiqueta, Medida, Producto
from applications.prov.models import Proveedor
from applications.users.models import User


class Orden_Compra_Estatus(ClaseModelo):
    nombre = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        super(Orden_Compra_Estatus, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural="Ordenes Compra Estatus"


SINO_CHOICES = (
        ('', 'Seleccione'),
        ('S', 'SI'),
        ('N', 'NO'), 
)
DIVISA_CHOICES = (
        ('', 'Seleccione'),
        ('P', 'Pesos (MXN)'),
        ('D', 'Dólares (USD)'), 
)
LAB_CHOICES = (
        ('', 'Seleccione'),
        ('E', 'Empaque'),
        ('P', 'Puesto en Bodega'), 
)


class Orden_Compra(ClaseModelo):
    consignacion = models.BooleanField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, blank=True, null=True)
    # libre_abordo = models.CharField(max_length=1, choices=LAB_CHOICES, blank=True, null=True)
    entregar_en = models.ForeignKey(Domicilio, on_delete=models.PROTECT, blank=True, null=True)
    fecha_entrega = models.DateField(auto_now=False,null=True,blank=True)
    comentario_oc= models.CharField(
        max_length=100, blank=True, null=True
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=True, null=True)
    divisa = models.CharField(max_length=1, choices=DIVISA_CHOICES, blank=True, null=True)
    tipo_cambio = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    comentario_pedido = models.CharField(
        max_length=100, blank=True, null=True
    )
    embarcador = models.ForeignKey(User,related_name='embarcador', on_delete=models.PROTECT, blank=True, null=True)
    comision = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    tarimas = models.PositiveIntegerField(default=0)
    cajas_tarimas = models.PositiveIntegerField(default=0)
    total_cajas = models.PositiveIntegerField(default=0)
    flete1 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    flete2 = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    aduana_mx = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    sobrepeso_mx = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    aduana_us = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    sobrepeso_us = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    logistica = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    otros = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    
    venta_consignacion = models.CharField(max_length=1, choices=SINO_CHOICES, blank=True)
    oc_local = models.CharField(max_length=1, choices=SINO_CHOICES, blank=True)

    total_precio_venta = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    total_comision = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    total_gasto = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    total_precio = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    total_cantidad = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    total_importe = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    estatus = models.ForeignKey(Orden_Compra_Estatus, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.proveedor.nombre
        
    def save(self):
        super(Orden_Compra, self).save()

    class Meta:
        verbose_name_plural="Ordenes Compra"



class Orden_Compra_Detalle(ClaseModelo):
    orden_compra = models.ForeignKey(Orden_Compra, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.PROTECT, blank=True, null=True)
    medida = models.ForeignKey(Medida, on_delete=models.PROTECT, blank=True, null=True)
    precio_venta = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    precio_reportar = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    comision = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    gasto = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    precio = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    cantidad = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    importe = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.producto
        
    def save(self):
        super(Orden_Compra_Detalle, self).save()

    class Meta:
        verbose_name_plural="Ordenes Compra Detalle"

