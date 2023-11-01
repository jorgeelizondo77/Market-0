from django.urls import path

from .views import (BancoView, BancoNew, BancoEdit, BancoDelete,
                    Forma_PagoView, Forma_PagoNew, Forma_PagoEdit, Forma_PagoDelete,
                    ProveedorView, ProveedorNew, ProveedorEdit, ProveedorDelete,
                    )

app_name = 'prov'

urlpatterns = [
    path('bancos/',BancoView.as_view(), name='banco_list'),
    path('banco/new/',BancoNew.as_view(), name='banco_new'),
    path('banco/edit/<int:pk>',BancoEdit.as_view(), name='banco_edit'),
    path('banco/delete/<int:id>',BancoDelete, name='banco_delete'),

    path('formas_pago/',Forma_PagoView.as_view(), name='forma_pago_list'),
    path('forma_pago/new/',Forma_PagoNew.as_view(), name='forma_pago_new'),
    path('forma_pago/edit/<int:pk>',Forma_PagoEdit.as_view(), name='forma_pago_edit'),
    path('forma_pago/delete/<int:id>',Forma_PagoDelete, name='forma_pago_delete'),

    path('proveedores/',ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new/',ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>',ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/delete/<int:id>',ProveedorDelete, name='proveedor_delete'),
]