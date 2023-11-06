from django.test import TestCase

from applications.dom.models import Pais


def setUp(self):
    self.pais = Pais(clave='223', nombre='México', uc_id=1)
    self.pais.save()


def test_creacion_de_pais(self):
        # Prueba de creación de un país
        pais = Pais.objects.create(clave='223', nombre='México', uc_id=1)
        self.assertEqual(pais.clave, '223')
        self.assertEqual(pais.nombre, 'México')


def test_lectura_de_pais(self):
        # Prueba de lectura de un país
        pais_leido = Pais.objects.get(clave='223')
        self.assertEqual(pais_leido.nombre, 'México')


def test_actualizacion_de_pais(self):
        # Prueba de actualización de un país
        self.pais.nombre = 'MEXICO'
        self.pais.save()
        pais_actualizado = Pais.objects.get(clave='223')
        self.assertEqual(pais_actualizado.nombre, 'MEXICO')

        