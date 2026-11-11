from django.db import models
from django.db.models import Count, Q
from django.urls import reverse
from django.utils import timezone


class IncidenciaQuerySet(models.QuerySet):
    def buscar(self, texto):
        if not texto:
            return self
        return self.filter(
            Q(codigo__icontains=texto)
            | Q(titulo__icontains=texto)
            | Q(solicitante__icontains=texto)
            | Q(dependencia__icontains=texto)
        )

    def filtrar(self, estado="", categoria="", prioridad=""):
        consulta = self
        if estado:
            consulta = consulta.filter(estado=estado)
        if categoria:
            consulta = consulta.filter(categoria=categoria)
        if prioridad:
            consulta = consulta.filter(prioridad=prioridad)
        return consulta

    def resumen(self):
        return self.aggregate(
            total=Count("id"),
            abiertas=Count("id", filter=Q(estado="abierta")),
            en_atencion=Count("id", filter=Q(estado="en_atencion")),
            resueltas=Count("id", filter=Q(estado__in=["resuelta", "cerrada"])),
        )

    def conteo_categorias(self):
        conteos = dict(
            self.order_by().values_list("categoria").annotate(total=Count("id"))
        )
        return [
            {
                "clave": clave,
                "etiqueta": etiqueta,
                "icono": self.model.ICONOS[clave],
                "total": conteos.get(clave, 0),
            }
            for clave, etiqueta in self.model.CATEGORIAS
        ]


class Incidencia(models.Model):
    CATEGORIAS = [
        ("red", "Red y conectividad"),
        ("correo", "Correo institucional"),
        ("campus", "Campus virtual"),
        ("equipos", "Equipos y laboratorios"),
        ("software", "Software y licencias"),
        ("academicos", "Sistemas académicos"),
    ]
    PRIORIDADES = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
        ("critica", "Crítica"),
    ]
    ESTADOS = [
        ("abierta", "Abierta"),
        ("en_atencion", "En atención"),
        ("resuelta", "Resuelta"),
        ("cerrada", "Cerrada"),
    ]
    ICONOS = {
        "red": "wifi",
        "correo": "mail",
        "campus": "graduation-cap",
        "equipos": "monitor",
        "software": "app-window",
        "academicos": "database",
    }

    codigo = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=140)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES, default="media")
    estado = models.CharField(max_length=12, choices=ESTADOS, default="abierta")
    solicitante = models.CharField(max_length=120)
    dependencia = models.CharField(max_length=120)
    ubicacion = models.CharField(max_length=120)
    fecha_reporte = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen_url = models.URLField(max_length=400, blank=True)

    objects = IncidenciaQuerySet.as_manager()

    class Meta:
        ordering = ["-fecha_reporte"]
        verbose_name = "incidencia"
        verbose_name_plural = "incidencias"

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"

    def get_absolute_url(self):
        return reverse("detalle", kwargs={"pk": self.pk})

    @property
    def es_urgente(self):
        return self.prioridad in ("alta", "critica") and self.estado in (
            "abierta",
            "en_atencion",
        )