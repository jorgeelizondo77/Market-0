from django.db import models
from applications.base.models import ClaseModelo
from applications.cli.models import Regimen
from applications.dom.models import Entidad, Municipio, Pais
from applications.prod.models import Categoria


class Banco(ClaseModelo):
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Banco, self).save()

    class Meta:
        verbose_name_plural="Bancos"



class Forma_Pago(ClaseModelo):
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Forma_Pago, self).save()

    class Meta:
        verbose_name_plural="Forma_Pago"



class Proveedor(ClaseModelo):
    nombre = models.CharField(
        max_length=100
    )
    rfc = models.CharField(
        max_length=13, blank=True, null=True
    )
    regimen = models.ForeignKey(Regimen, on_delete=models.PROTECT, blank=True, null=True)

    contacto_embarque = models.CharField(
        max_length=100, blank=True, null=True
    )
    correo = models.EmailField(blank=True, null=True)
    t_celular = models.CharField(
        max_length=50, blank=True, null=True
    )
    t_oficina = models.CharField(
        max_length=50, blank=True, null=True
    )

    calle = models.CharField(
        max_length=50, blank=True, null=True
    )
    numero_externo = models.CharField(
        max_length=10, blank=True, null=True
    )
    numero_interno = models.CharField(
        max_length=10, blank=True, null=True
    )

    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, blank=True, null=True)

    colonia = models.CharField(
        max_length=60, blank=True, null=True
    )
    cp = models.CharField(
        max_length=10, blank=True, null=True
    )
    zona = models.CharField(
        max_length=20, blank=True, null=True
    )

    categorias = models.ManyToManyField(Categoria)

    contacto_venta = models.CharField(
        max_length=100, blank=True, null=True
    )
    correo_venta = models.EmailField(blank=True, null=True)
    t_celular_venta = models.CharField(
        max_length=50, blank=True, null=True
    )
    t_oficina_venta = models.CharField(
        max_length=50, blank=True, null=True
    )

    forma_pago = models.ForeignKey(Forma_Pago, on_delete=models.PROTECT, blank=True, null=True)
    plazo = models.PositiveIntegerField(default=0, blank=True, null=True)
    descuento = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    limite_credito = models.PositiveIntegerField(default=0, blank=True, null=True)

    banco = models.ForeignKey(Banco, on_delete=models.PROTECT, blank=True, null=True)
    cuenta_banco = models.CharField(
        max_length=20, blank=True, null=True
    )
    clabe = models.CharField(max_length=20, blank=True, null=True)

    comentario = models.CharField(
        max_length=100, blank=True, null=True
    )

    def __str__(self):
        return self.nombre
        
    def save(self):
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural="Proveedores"
