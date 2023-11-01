from django.contrib import admin

from applications.prod.models import Unidad_Compra,Categoria,Producto

admin.site.register(Unidad_Compra)
admin.site.register(Categoria)
admin.site.register(Producto)
