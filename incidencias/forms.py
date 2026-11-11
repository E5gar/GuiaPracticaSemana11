from django import forms

from .models import Incidencia


class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = [
            "titulo",
            "descripcion",
            "categoria",
            "prioridad",
            "solicitante",
            "dependencia",
            "ubicacion",
        ]