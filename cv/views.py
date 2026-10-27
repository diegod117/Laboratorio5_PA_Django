from django.shortcuts import render


def home(request):
    """Página de inicio: lista de integrantes con enlace a su CV.

    Para agregar un integrante, añadir un dict a `integrantes` (o su enlace en home.html).
    """
    integrantes = [
        {'nombre': 'CV de ejemplo', 'url_name': 'cv_ejemplo'},
        {'nombre': 'Johann Cortes', 'url_name': 'cv_johann'},
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


def cv_johann(request):
    """CV de Johann Cortés Farias."""
    contexto = {
        'nombre': 'Johann Cortés Farias',
        'edad': 22,
        'titulo': 'Estudiante de Ingeniería Civil en Computación e Informática',
        'contacto': {
            'email': 'johann.cortes@alumnos.ucentral.cl',
            'ciudad': 'Monte Patria, Chile',
        },
        'habilidades': ['Python', 'Django', 'React', 'HTML y CSS', 'Git y GitHub'],
        'experiencia': [
            {
                'cargo': 'Desarrollador de Geocuartel',
                'empresa': 'Proyecto personal',
                'descripcion': (
                    'Aplicación web para el monitoreo de estados fenológicos y plagas '
                    'en cultivos de mandarinas y uvas. Registra por cuartel lo observado '
                    'en terreno para comparar temporadas y decidir a tiempo las aplicaciones.'
                ),
                'detalle': (
                    'Geocuartel registra por cuartel el estado fenológico del cultivo y '
                    'las plagas observadas, con fecha y ubicación, para comparar temporadas '
                    'y decidir a tiempo las aplicaciones. Fue desarrollada para mi papá y '
                    'centraliza la información en una base de datos accesible desde la web.'
                ),
            },
        ],
    }
    return render(request, 'cv/cv_johann.html', contexto)
