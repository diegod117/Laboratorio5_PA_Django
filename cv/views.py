from django.shortcuts import render


def home(request):
    """Página de inicio: lista de integrantes con enlace a su CV.

    Para agregar un integrante, añadir un dict a `integrantes` (o su enlace en home.html).
    """
    integrantes = [
        {'nombre': 'CV de ejemplo', 'url_name': 'cv_ejemplo'},
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


def cv_diego(request):
    """CV de Diego Cortés Toro."""
    contexto = {
        'nombre': 'Diego Cortés Toro',
        'titulo': 'Estudiante de Ingeniería Civil en Computación e Informática',
        'contacto': {
            'email': 'diegocortt@gmail.com',
            'telefono': '958568957',
            'ciudad': 'La Reconquista 1738, La Serena',
        },
        'habilidades': [
            'Java', 'Python', 'C', 'C++',
            'Diseño y modelado de datos, SQL, consultas y optimización',
            'Armado y ensamblaje de computadoras',
            'IoT y embebidos: Arduino',
        ],
        'experiencia': [
            {
                'cargo': 'Desarrollo e Integración de Sistemas',
                'empresa': 'Universidad Central | La Serena',
                'periodo': '2025',
                'descripcion': 'Proyecto de programación en equipos multidisciplinarios. '
                               'Aplicación de conceptos de Ingeniería de Software en contextos académicos.',
            },
            {
                'cargo': 'Prototipado con Arduino e IoT',
                'empresa': 'Universidad Central | La Serena',
                'periodo': '2025',
                'descripcion': 'Diseño e implementación de prototipos basados en Arduino, '
                               'con integración de sensores y sistemas de automatización.',
            },
        ],
    }
    return render(request, 'cv/cv_diego.html', contexto)

