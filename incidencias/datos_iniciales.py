from datetime import timedelta

from django.utils import timezone

from .models import Incidencia


def foto(identificador):
    return f"https://images.unsplash.com/{identificador}?auto=format&fit=crop&w=1200&q=70"


DATOS = [
    {
        "codigo": "OTI-2026-0001",
        "titulo": "Caída del Wi-Fi en el pabellón de Sistemas",
        "descripcion": "Desde las 8:00 los puntos de acceso del segundo piso no entregan dirección IP. Los estudiantes no pueden conectarse durante las clases de laboratorio.",
        "categoria": "red",
        "prioridad": "alta",
        "estado": "en_atencion",
        "solicitante": "marco antonio quispe rojas",
        "dependencia": "Facultad de Ingeniería de Sistemas",
        "ubicacion": "Pabellón B, segundo piso",
        "horas": 5,
        "imagen_url": foto("photo-1451187580459-43490279c0fa"),
    },
    {
        "codigo": "OTI-2026-0002",
        "titulo": "Sin acceso al correo institucional de docentes",
        "descripcion": "Varios docentes reciben error de credenciales al ingresar al correo desde el navegador y desde el celular, tras el cambio de contraseña obligatorio.",
        "categoria": "correo",
        "prioridad": "media",
        "estado": "abierta",
        "solicitante": "lucia fernanda ccora huaman",
        "dependencia": "Facultad de Derecho y Ciencias Políticas",
        "ubicacion": "Oficina de decanato",
        "horas": 22,
        "imagen_url": foto("photo-1488590528505-98d2b5aba04b"),
    },
    {
        "codigo": "OTI-2026-0003",
        "titulo": "Aula virtual no carga las evaluaciones del curso",
        "descripcion": "El examen parcial del curso de Estadística queda en blanco al abrirlo. Hay cuarenta estudiantes citados para rendirlo esta tarde.",
        "categoria": "campus",
        "prioridad": "critica",
        "estado": "abierta",
        "solicitante": "jorge luis vilcahuaman paucar",
        "dependencia": "Facultad de Ingeniería Química",
        "ubicacion": "Laboratorio de cómputo 2",
        "horas": 2,
        "imagen_url": foto("photo-1517694712202-14dd9538aa97"),
    },
    {
        "codigo": "OTI-2026-0004",
        "titulo": "Computadoras del laboratorio no encienden",
        "descripcion": "Seis equipos del laboratorio 3 no pasan del arranque tras un corte eléctrico. Se necesita revisión de fuentes y memoria.",
        "categoria": "equipos",
        "prioridad": "alta",
        "estado": "en_atencion",
        "solicitante": "carmen rosa baldeón ticse",
        "dependencia": "Facultad de Ingeniería Civil",
        "ubicacion": "Laboratorio 3",
        "horas": 30,
        "imagen_url": foto("photo-1593642632823-8f785ba67e45"),
    },
    {
        "codigo": "OTI-2026-0005",
        "titulo": "Licencia de software de diseño vencida",
        "descripcion": "El software de diseño asistido muestra el aviso de licencia expirada y bloquea el guardado de proyectos de los estudiantes.",
        "categoria": "software",
        "prioridad": "media",
        "estado": "resuelta",
        "solicitante": "daniel esteban melgar yupanqui",
        "dependencia": "Facultad de Ingeniería Mecánica",
        "ubicacion": "Taller de diseño",
        "horas": 70,
        "imagen_url": foto("photo-1461749280684-dccba630e2f6"),
    },
    {
        "codigo": "OTI-2026-0006",
        "titulo": "Error al registrar notas en el sistema académico",
        "descripcion": "Al guardar el acta de notas aparece un error interno y el registro no se completa. El plazo de cierre vence mañana.",
        "categoria": "academicos",
        "prioridad": "critica",
        "estado": "en_atencion",
        "solicitante": "patricia milagros arauco soto",
        "dependencia": "Dirección de Registros Académicos",
        "ubicacion": "Oficina de registros",
        "horas": 3,
        "imagen_url": foto("photo-1544197150-b99a580bb7a8"),
    },
    {
        "codigo": "OTI-2026-0007",
        "titulo": "Punto de red sin señal en la biblioteca central",
        "descripcion": "El punto de red del módulo de atención no reconoce el cable. El equipo de préstamos trabaja sin acceso al catálogo.",
        "categoria": "red",
        "prioridad": "media",
        "estado": "abierta",
        "solicitante": "walter hugo camayo lazo",
        "dependencia": "Biblioteca Central",
        "ubicacion": "Módulo de préstamos",
        "horas": 18,
        "imagen_url": foto("photo-1518770660439-4636190af475"),
    },
    {
        "codigo": "OTI-2026-0008",
        "titulo": "Proyector multimedia sin imagen en el auditorio",
        "descripcion": "El proyector enciende pero no detecta la señal HDMI. Hay una conferencia programada para la mañana siguiente.",
        "categoria": "equipos",
        "prioridad": "alta",
        "estado": "abierta",
        "solicitante": "ana maría tovar chávez",
        "dependencia": "Facultad de Medicina Humana",
        "ubicacion": "Auditorio principal",
        "horas": 9,
        "imagen_url": foto("photo-1531297484001-80022131f5a1"),
    },
    {
        "codigo": "OTI-2026-0009",
        "titulo": "Solicitud de nuevas cuentas para ingresantes",
        "descripcion": "Se requiere crear las cuentas de correo institucional del grupo de ingresantes de la escuela de Zootecnia antes del inicio de clases.",
        "categoria": "correo",
        "prioridad": "baja",
        "estado": "resuelta",
        "solicitante": "raúl alberto espinoza mayta",
        "dependencia": "Facultad de Zootecnia",
        "ubicacion": "Secretaría académica",
        "horas": 96,
        "imagen_url": foto("photo-1526374965328-7f61d4dc18c5"),
    },
    {
        "codigo": "OTI-2026-0010",
        "titulo": "Intento de acceso sospechoso a cuenta administrativa",
        "descripcion": "Se detectaron varios intentos fallidos desde una ubicación desconocida contra una cuenta del área administrativa. Se solicita bloqueo y revisión.",
        "categoria": "software",
        "prioridad": "critica",
        "estado": "cerrada",
        "solicitante": "elena victoria paredes inga",
        "dependencia": "Oficina de Recursos Humanos",
        "ubicacion": "Oficina administrativa",
        "horas": 140,
        "imagen_url": foto("photo-1563986768609-322da13575f3"),
    },
    {
        "codigo": "OTI-2026-0011",
        "titulo": "Matrícula en línea muestra cursos duplicados",
        "descripcion": "Algunos estudiantes ven el mismo curso dos veces en su ficha de matrícula y el sistema impide confirmar el registro.",
        "categoria": "academicos",
        "prioridad": "alta",
        "estado": "abierta",
        "solicitante": "kevin andré lazo bonilla",
        "dependencia": "Facultad de Ingeniería de Sistemas",
        "ubicacion": "Atención al estudiante",
        "horas": 12,
        "imagen_url": foto("photo-1498050108023-c5249f4df085"),
    },
    {
        "codigo": "OTI-2026-0012",
        "titulo": "Actualización de equipos del laboratorio de redes",
        "descripcion": "Se solicita actualizar el sistema operativo y las herramientas de simulación en veinte equipos antes de la práctica calificada.",
        "categoria": "software",
        "prioridad": "baja",
        "estado": "en_atencion",
        "solicitante": "silvia noemí quinto arroyo",
        "dependencia": "Facultad de Ingeniería Eléctrica y Electrónica",
        "ubicacion": "Laboratorio de redes",
        "horas": 48,
        "imagen_url": foto("photo-1587829741301-dc798b83add3"),
    },
]


def cargar():
    ahora = timezone.now()
    creadas = 0
    for dato in DATOS:
        valores = dict(dato)
        horas = valores.pop("horas")
        codigo = valores.pop("codigo")
        valores["fecha_reporte"] = ahora - timedelta(hours=horas)
        _, nueva = Incidencia.objects.update_or_create(
            codigo=codigo, defaults=valores
        )
        if nueva:
            creadas += 1
    return creadas