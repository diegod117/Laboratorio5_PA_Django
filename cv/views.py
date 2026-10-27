from django.shortcuts import render


def home(request):
    """Página de inicio: lista de integrantes con enlace a su CV.

    Para agregar un integrante, añadir un dict a `integrantes` (o su enlace en home.html).
    """
    integrantes = [
        {'nombre': 'CV de ejemplo', 'url_name': 'cv_ejemplo'},
        {'nombre': 'Diego Cortés Toro', 'url_name': 'cv_diego'},
    ]
    return render(request, 'home.html', {'integrantes': integrantes})


def cv_ejemplo(request):
    """CV de ejemplo: patrón que cada integrante repite con sus propios datos."""
    contexto = {
        'nombre': 'Juan Pérez',
        'titulo': 'Ingeniero en Informática',
        'contacto': {
            'email': 'juan.perez@ejemplo.cl',
            'telefono': '+56 9 1234 5678',
            'ciudad': 'Santiago, Chile',
        },
        'habilidades': ['Python', 'Django', 'HTML y CSS', 'Git y GitHub', 'SQL'],
        'experiencia': [
            {
                'cargo': 'Desarrollador Junior',
                'empresa': 'Tech Ejemplo SpA',
                'periodo': '2024 - Actualidad',
                'descripcion': 'Desarrollo de aplicaciones web con Django.',
            },
            {
                'cargo': 'Practicante de Software',
                'empresa': 'Soluciones Demo Ltda.',
                'periodo': '2023 - 2024',
                'descripcion': 'Apoyo en pruebas y mantenimiento de sistemas internos.',
            },
        ],
    }
    return render(request, 'cv/cv_ejemplo.html', contexto)

from django.shortcuts import render

# (Aquí arriba deberían estar las vistas de home y cv_ejemplo)

def cv_martin(request):
    contexto = {
        'nombre': 'Martín Alexis Francisco Zepeda Puelles',
        'titulo': 'Estudiante de 4to año - Ingeniería Civil en Computación e Informática',
        'contacto': 'La Florida, La Serena / El Salvador | Certificación IBM Project Management Professional',
        'habilidades': [
            'Análisis de datos: Power BI, Microsoft Excel, SQL',
            'Desarrollo Web: HTML, CSS, JavaScript (Manipulación de DOM)',
            'Python (Pygame, Machine Learning en Google Colab)',
            'Herramientas: GitHub, Figma, Arduino'
        ],
        'experiencia': [
            'Práctica Operacional en Codelco División Salvador: Creación de dashboards dinámicos en Power BI conectados vía APIs HTTPS.',
            'Desarrollo de prototipo web interactivo para gestión de inventarios y reservas de laboratorios (Universidad Central).',
            'Diseño de modelo conceptual y Lean Canvas para plataforma comparadora de precios de Pokémon TCG en Chile.',
            'Programación de videojuego Tower Defense utilizando Python y Pygame.',
            'Diseño de interfaz digital en Figma para ferretería local.'
        ]
    }
    return render(request, 'cv/cv_martin.html', contexto)
