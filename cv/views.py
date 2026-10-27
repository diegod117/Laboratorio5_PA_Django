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
