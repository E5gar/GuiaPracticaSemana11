from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="inicio"),
    path("incidencias/", views.IncidenciaListView.as_view(), name="catalogo"),
    path("incidencias/<int:pk>/", views.IncidenciaDetailView.as_view(), name="detalle"),
    path("servicios/", views.servicios, name="servicios"),
    path("contacto/", views.contacto, name="contacto"),
]