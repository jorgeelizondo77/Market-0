from django.urls import path

from .views import (PaisView, PaisNew, PaisEdit, PaisDelete,
                    EntidadView, EntidadNew, EntidadEdit, EntidadDelete,
                    MunicipioView, MunicipioNew, MunicipioEdit, MunicipioDelete, 
                    get_entidades, get_municipios,
                    DomicilioView, DomicilioNew, DomicilioEdit, DomicilioDelete,
                    ZonaView, ZonaNew, ZonaEdit, ZonaDelete
                    )

app_name = 'dom'

urlpatterns = [
    path('paises/',PaisView.as_view(), name='pais_list'),
    path('pais/new/',PaisNew.as_view(), name='pais_new'),
    path('pais/edit/<int:pk>',PaisEdit.as_view(), name='pais_edit'),
    path('pais/delete/<int:id>',PaisDelete, name='pais_delete'),

    path('entidades/',EntidadView.as_view(), name='entidad_list'),
    path('entidad/new/',EntidadNew.as_view(), name='entidad_new'),
    path('entidad/edit/<int:pk>',EntidadEdit.as_view(), name='entidad_edit'),
    path('entidad/delete/<int:id>',EntidadDelete, name='entidad_delete'),

    path('municipios/',MunicipioView.as_view(), name='municipio_list'),
    path('municipio/new/',MunicipioNew.as_view(), name='municipio_new'),
    path('municipio/edit/<int:pk>',MunicipioEdit.as_view(), name='municipio_edit'),
    path('municipio/delete/<int:id>',MunicipioDelete, name='municipio_delete'),

    path('get_entidades/', get_entidades, name='get_entidades'),
    path('get_municipios/', get_municipios, name='get_municipios'),

    path('domicilios/',DomicilioView.as_view(), name='domicilio_list'),
    path('domicilio/new/',DomicilioNew.as_view(), name='domicilio_new'),
    path('domicilio/edit/<int:pk>',DomicilioEdit.as_view(), name='domicilio_edit'),
    path('domicilio/delete/<int:id>',DomicilioDelete, name='domicilio_delete'),

    path('zonas/',ZonaView.as_view(), name='zona_list'),
    path('zona/new/',ZonaNew.as_view(), name='zona_new'),
    path('zona/edit/<int:pk>',ZonaEdit.as_view(), name='zona_edit'),
    path('zona/delete/<int:id>',ZonaDelete, name='zona_delete'),

]