from django.contrib import admin

from .models import Incidencia


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "titulo",
        "categoria",
        "prioridad",
        "estado",
        "dependencia",
        "fecha_reporte",
    )
    list_filter = ("estado", "prioridad", "categoria")
    search_fields = ("codigo", "titulo", "solicitante", "dependencia")
    date_hierarchy = "fecha_reporte"