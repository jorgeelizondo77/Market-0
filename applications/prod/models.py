from django.db import models
from applications.base.models import ClaseModelo



class Unidad_Compra(ClaseModelo):
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Unidad_Compra, self).save()

    class Meta:
        verbose_name_plural="Unidad_Compra"
          


class Categoria(ClaseModelo):
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural="Categorias"



class Producto(ClaseModelo):
    nombre = models.CharField(
        max_length=60
    )
    sku = models.CharField(
        max_length=20
    )
    upc = models.CharField(
        max_length=20
    )
    cuenta_contable = models.CharField(
        max_length=20, blank=True, null=True
    )

    numero_sat = models.CharField(
        max_length=20, blank=True, null=True
    )
    unidad_sat = models.CharField(
        max_length=20, blank=True, null=True
    )
    qrcaja = models.CharField(
        max_length=20, blank=True, null=True
    )
    qrpalet = models.CharField(
        max_length=20, blank=True, null=True
    )

    unidad_compra = models.ForeignKey(Unidad_Compra, on_delete=models.PROTECT, blank=True, null=True)
    costo_promedio = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    unidad_venta = models.ForeignKey(Unidad_Compra, related_name="unidad_venta", on_delete=models.PROTECT, blank=True, null=True)
    margen = models.DecimalField(default=0, max_digits=12, decimal_places=2)
   
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, blank=True, null=True)
    comentario = models.CharField(
        max_length=100, blank=True, null=True
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Producto, self).save()

    class Meta:
        verbose_name_plural="Productos"


class Etiqueta(ClaseModelo):
    nombre = models.CharField(
        max_length=30
    )
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre
        
    def save(self):
        super(Etiqueta, self).save()

    class Meta:
        verbose_name_plural="Etiquetas"



class Medida(ClaseModelo):
    nombre = models.CharField(
        max_length=30
    )
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre
        
    def save(self):
        super(Medida, self).save()

    class Meta:
        verbose_name_plural="Medidas"



