from django.urls import path

from .views import (ClienteNew, ClienteView, ClienteEdit, ClienteDelete,
                    RegimenView, RegimenNew, RegimenEdit, RegimenDelete
                    )

app_name = 'cli'

urlpatterns = [
    path('regimenes/',RegimenView.as_view(), name='regimen_list'),
    path('regimen/new/',RegimenNew.as_view(), name='regimen_new'),
    path('regimen/edit/<int:pk>',RegimenEdit.as_view(), name='regimen_edit'),
    path('regimen/delete/<int:id>',RegimenDelete, name='regimen_delete'),

    path('clientes/',ClienteView.as_view(), name='cliente_list'),
    path('cliente/new/',ClienteNew.as_view(), name='cliente_new'),
    path('cliente/edit/<int:pk>',ClienteEdit.as_view(), name='cliente_edit'),
    path('cliente/delete/<int:id>',ClienteDelete, name='cliente_delete'),

]