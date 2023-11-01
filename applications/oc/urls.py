from django.urls import path

from .views import (Orden_CompraView,Orden_CompraNew,Orden_CompraEdit,
                    Orden_CompraPdfView,
                    guarda_oc_detalle, elimina_oc_detalle)

app_name = 'oc'

urlpatterns = [
    path('orders/',Orden_CompraView.as_view(), name='occ_list'),
    path('order/new/',Orden_CompraNew.as_view(), name='occ_new'),
    path('order/edit/<int:pk>',Orden_CompraEdit.as_view(), name='occ_edit'),
    path('guarda_oc_detalle/', guarda_oc_detalle, name='guarda_oc_detalle'),
    path('elimina_oc_detalle/', elimina_oc_detalle, name='elimina_oc_detalle'),
    path('order/pdf/<int:pk>',Orden_CompraPdfView.as_view(), name='occ_report'),
]