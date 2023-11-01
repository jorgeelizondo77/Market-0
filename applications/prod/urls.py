from django.urls import path

from .views import (Unidad_CompraView, Unidad_CompraNew, Unidad_CompraEdit, Unidad_CompraDelete,
                    CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete, 
                    ProductoView, ProductoNew, ProductoEdit, ProductoDelete,get_productos,
                    EtiquetaView, EtiquetaNew, EtiquetaEdit, EtiquetaDelete,
                    MedidaView, MedidaNew, MedidaEdit, MedidaDelete
                    )

app_name = 'prod'

urlpatterns = [
    path('unidades_compra/',Unidad_CompraView.as_view(), name='unidad_compra_list'),
    path('unidad_compra/new/',Unidad_CompraNew.as_view(), name='unidad_compra_new'),
    path('unidad_compra/edit/<int:pk>',Unidad_CompraEdit.as_view(), name='unidad_compra_edit'),
    path('unidad_compra/delete/<int:id>',Unidad_CompraDelete, name='unidad_compra_delete'),

    path('categorias/',CategoriaView.as_view(), name='categoria_list'),
    path('categoria/new/',CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>',CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/delete/<int:id>',CategoriaDelete, name='categoria_delete'),

    path('productos/',ProductoView.as_view(), name='producto_list'),
    path('producto/new/',ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>',ProductoEdit.as_view(), name='producto_edit'),
    path('producto/delete/<int:id>',ProductoDelete, name='producto_delete'),

    path('get_productos/', get_productos, name='get_productos'),

    path('etiquetas/',EtiquetaView.as_view(), name='etiqueta_list'),
    path('etiqueta/new/',EtiquetaNew.as_view(), name='etiqueta_new'),
    path('etiqueta/edit/<int:pk>',EtiquetaEdit.as_view(), name='etiqueta_edit'),
    path('etiqueta/delete/<int:id>',EtiquetaDelete, name='etiqueta_delete'),

    path('medidas/',MedidaView.as_view(), name='medida_list'),
    path('medida/new/',MedidaNew.as_view(), name='medida_new'),
    path('medida/edit/<int:pk>',MedidaEdit.as_view(), name='medida_edit'),
    path('medida/delete/<int:id>',MedidaDelete, name='medida_delete'),

]