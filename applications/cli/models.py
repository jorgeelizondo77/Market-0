from django.db import models
from applications.base.models import ClaseModelo
from applications.dom.models import Entidad, Municipio, Pais, Zona


class Regimen(ClaseModelo):
    clave = models.CharField(
        max_length=3,
        default=0
    )
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Regimen, self).save()

    class Meta:
        verbose_name_plural="Regimen"



class Cliente(ClaseModelo):
    nombre = models.CharField(
        max_length=100
    )
    rfc = models.CharField(
        max_length=13, blank=True, null=True
    )
    regimen = models.ForeignKey(Regimen, on_delete=models.PROTECT, blank=True, null=True)
    
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
    zona = models.ForeignKey(Zona, on_delete=models.PROTECT, blank=True, null=True)

    contacto = models.CharField(
        max_length=100, blank=True, null=True
    )
    correo = models.EmailField(blank=True, null=True)
    t_celular = models.CharField(
        max_length=50, blank=True, null=True
    )
    
    t_oficina = models.CharField(
        max_length=50, blank=True, null=True
    )
    t_casa = models.CharField(
        max_length=50, blank=True, null=True
    )
    cuenta_contable = models.CharField(
        max_length=20, blank=True, null=True
    )

    plazo = models.PositiveIntegerField(default=0, blank=True, null=True)
    comentario = models.CharField(
        max_length=100, blank=True, null=True
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural="Clientes"
