from django.db import models
from applications.base.models import ClaseModelo



class Pais(ClaseModelo):
    clave = models.CharField(
        max_length=3
    )
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Pais, self).save()

    class Meta:
        verbose_name_plural="Paises"



class Entidad(ClaseModelo):
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    clave = models.CharField(
        max_length=3
    )
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Entidad, self).save()

    class Meta:
        verbose_name_plural="Entidades"




class Municipio(ClaseModelo):
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT)
    clave = models.CharField(
        max_length=3
    )
    nombre = models.CharField(
        max_length=60
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Municipio, self).save()

    class Meta:
        verbose_name_plural="Municipios"



class Domicilio(ClaseModelo):
    nombre = models.CharField(
        max_length=50
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

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Domicilio, self).save()

    class Meta:
        verbose_name_plural="Domicilios"


class Zona(ClaseModelo):
    nombre = models.CharField(
        max_length=50
    )

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        super(Zona, self).save()

    class Meta:
        verbose_name_plural="Zonas"