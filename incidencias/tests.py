from django.test import TestCase
from django.urls import reverse

from .models import Incidencia


class RutasTest(TestCase):
    def setUp(self):
        self.incidencia = Incidencia.objects.create(
            codigo="OTI-TEST-0001",
            titulo="Prueba de red",
            descripcion="Detalle de prueba",
            categoria="red",
            prioridad="alta",
            estado="abierta",
            solicitante="usuario de prueba",
            dependencia="Oficina de prueba",
            ubicacion="Laboratorio 1",
        )

    def test_paginas_responden(self):
        for nombre in ["inicio", "catalogo", "servicios", "contacto"]:
            respuesta = self.client.get(reverse(nombre))
            self.assertEqual(respuesta.status_code, 200)

    def test_detalle(self):
        respuesta = self.client.get(reverse("detalle", args=[self.incidencia.pk]))
        self.assertContains(respuesta, "OTI-TEST-0001")

    def test_filtro_por_estado(self):
        respuesta = self.client.get(reverse("catalogo"), {"estado": "cerrada"})
        self.assertNotContains(respuesta, "OTI-TEST-0001")

    def test_consultas_del_modelo(self):
        self.assertEqual(Incidencia.objects.filtrar(estado="abierta").count(), 1)
        self.assertEqual(Incidencia.objects.resumen()["abiertas"], 1)