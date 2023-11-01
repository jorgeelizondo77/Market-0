from django.contrib import admin

from applications.prov.models import Banco, Forma_Pago, Proveedor

admin.site.register(Banco)
admin.site.register(Forma_Pago)
admin.site.register(Proveedor)
