from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Incidencia

SERVICIOS = [
    {
        "icono": "wifi",
        "titulo": "Red y conectividad",
        "descripcion": "Cobertura inalámbrica, puntos de red cableados y acceso a internet en pabellones, aulas y oficinas.",
        "incluye": [
            "Diagnóstico de puntos de acceso",
            "Reubicación y configuración de puntos de red",
            "Seguimiento de caídas por pabellón",
        ],
        "imagen": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=70",
    },
    {
        "icono": "mail",
        "titulo": "Correo institucional",
        "descripcion": "Cuentas de docentes, administrativos y estudiantes, con recuperación de acceso y control de cuotas.",
        "incluye": [
            "Restablecimiento de contraseñas",
            "Creación y baja de cuentas",
            "Listas de distribución por dependencia",
        ],
        "imagen": "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?auto=format&fit=crop&w=1200&q=70",
    },
    {
        "icono": "graduation-cap",
        "titulo": "Campus virtual",
        "descripcion": "Soporte a las aulas virtuales, matrícula de cursos, carga de materiales y evaluaciones en línea.",
        "incluye": [
            "Alta de cursos y secciones",
            "Recuperación de actividades y notas",
            "Apoyo en evaluaciones programadas",
        ],
        "imagen": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=70",
    },
    {
        "icono": "monitor",
        "titulo": "Equipos y laboratorios",
        "descripcion": "Mantenimiento correctivo de computadoras, proyectores e impresoras en laboratorios y oficinas.",
        "incluye": [
            "Revisión de hardware",
            "Reinstalación de sistemas",
            "Préstamo temporal de equipos",
        ],
        "imagen": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=1200&q=70",
    },
    {
        "icono": "app-window",
        "titulo": "Software y licencias",
        "descripcion": "Instalación, activación y actualización de software académico y administrativo autorizado.",
        "incluye": [
            "Instalación en laboratorios",
            "Gestión de licencias institucionales",
            "Actualizaciones programadas",
        ],
        "imagen": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1200&q=70",
    },
    {
        "icono": "database",
        "titulo": "Sistemas académicos",
        "descripcion": "Atención de fallas en matrícula, registro de notas, constancias y demás sistemas internos.",
        "incluye": [
            "Corrección de datos mediante solicitud",
            "Soporte en periodos de matrícula",
            "Respaldo y restauración de información",
        ],
        "imagen": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1200&q=70",
    },
]

TIEMPOS = [
    {
        "prioridad": "critica",
        "etiqueta": "Crítica",
        "respuesta": "Menos de 1 hora",
        "detalle": "Servicio caído que afecta a toda una sede o dependencia.",
    },
    {
        "prioridad": "alta",
        "etiqueta": "Alta",
        "respuesta": "Hasta 4 horas",
        "detalle": "Falla que impide trabajar a un área o a un laboratorio completo.",
    },
    {
        "prioridad": "media",
        "etiqueta": "Media",
        "respuesta": "Hasta 1 día hábil",
        "detalle": "Problema que afecta a una persona pero tiene alternativa temporal.",
    },
    {
        "prioridad": "baja",
        "etiqueta": "Baja",
        "respuesta": "Hasta 3 días hábiles",
        "detalle": "Consultas, mejoras y solicitudes sin impacto en la operación.",
    },
]


def home(request):
    contexto = {
        "resumen": Incidencia.objects.resumen(),
        "categorias": Incidencia.objects.conteo_categorias(),
        "recientes": Incidencia.objects.all()[:6],
    }
    return render(request, "incidencias/inicio.html", contexto)


def servicios(request):
    contexto = {"servicios": SERVICIOS, "tiempos": TIEMPOS}
    return render(request, "incidencias/servicios.html", contexto)


def contacto(request):
    return render(request, "incidencias/contacto.html")


class IncidenciaListView(ListView):
    model = Incidencia
    template_name = "incidencias/catalogo.html"
    context_object_name = "incidencias"
    paginate_by = 9

    def leer_filtros(self):
        datos = self.request.GET
        return {
            "q": datos.get("q", "").strip(),
            "estado": datos.get("estado", ""),
            "categoria": datos.get("categoria", ""),
            "prioridad": datos.get("prioridad", ""),
        }

    def get_queryset(self):
        filtros = self.leer_filtros()
        return Incidencia.objects.buscar(filtros["q"]).filtrar(
            estado=filtros["estado"],
            categoria=filtros["categoria"],
            prioridad=filtros["prioridad"],
        )

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        parametros = self.request.GET.copy()
        parametros.pop("page", None)
        filtros = self.leer_filtros()
        contexto["filtros"] = filtros
        contexto["hay_filtros"] = any(filtros.values())
        contexto["querystring"] = parametros.urlencode()
        contexto["opciones"] = {
            "estados": Incidencia.ESTADOS,
            "categorias": Incidencia.CATEGORIAS,
            "prioridades": Incidencia.PRIORIDADES,
        }
        return contexto


class IncidenciaDetailView(DetailView):
    model = Incidencia
    template_name = "incidencias/detalle.html"
    context_object_name = "incidencia"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["relacionadas"] = Incidencia.objects.filter(
            categoria=self.object.categoria
        ).exclude(pk=self.object.pk)[:3]
        return contexto