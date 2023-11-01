from django.contrib import admin

from applications.dom.models import Pais, Entidad, Municipio, Domicilio, Zona


admin.site.register(Pais)
admin.site.register(Entidad)
admin.site.register(Municipio)
admin.site.register(Domicilio)
admin.site.register(Zona)
