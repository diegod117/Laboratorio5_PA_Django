from django.shortcuts import render


def home(request):
    """Página de inicio: lista de integrantes con enlace a su CV.

    Para agregar un integrante, añadir un dict a `integrantes` (o su enlace en home.html).
    """
    integrantes = [
        {'nombre': 'CV de ejemplo', 'url_name': 'cv_ejemplo'},
        {'nombre': 'Johann Cortés Farias', 'url_name': 'cv_johann'},
        {'nombre': 'Martín Zepeda', 'url_name': 'cv_martin'},
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


def cv_johann(request):
    """CV de Johann Cortés Farias."""
    contexto = {
        'nombre': 'Johann Cortés Farias',
        'edad': 22,
        'foto': 'img/pfp.png',
        'titulo': 'Estudiante de Ingeniería Civil en Computación e Informática',
        'contacto': {
            'email': 'johann.cortes@alumnos.ucentral.cl',
            'ciudad': 'Monte Patria, Chile',
        },
        'habilidades': ['Python', 'Django', 'React', 'HTML y CSS', 'Git y GitHub'],
        'educacion': [
            {
                'institucion': 'Universidad Central',
                'logo': 'img/ucentral.png',
                'periodo': '2023 - 2026',
                'titulo': 'Pregrado de Ingeniería Civil en Computación e Informática',
            },
        ],
        'experiencia': [
            {
                'cargo': 'Personal de temporada · Exportación de fruta',
                'empresa': 'Agrícola Bauzá',
                'logo': 'img/bauza.jpg',
                'periodo': '2022 - 2026 · Temporadas de verano (enero a febrero)',
                'descripcion': (
                    'Participación en la cadena de exportación de fruta durante '
                    'cuatro temporadas de verano.'
                ),
                'funciones': [
                    'Despacho de camiones de fruta con destino al extranjero, '
                    'con foco en la exportación.',
                    'Recepción de camiones en frigoríficos.',
                    'Encargado de las inspecciones SAG de exportación.',
                ],
            },
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




def cv_martin(request):
    """CV de Martín Zepeda."""
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
        'sobre_mi': 'Estudiante de Ingeniería Civil en Computación e Informática (4° año) con sólida '
                    'formación en programación, desarrollo de sistemas y hardware. Motivado por aprender el '
                    'funcionamiento interno de empresas tecnológicas y desarrollarme en un entorno laboral real. '
                    'Capacidad comprobada de trabajar en equipo, comunicarme efectivamente y adaptarme a nuevos '
                    'desafíos.',
        'educacion': {
            'institucion': 'Universidad Central de Chile - Sede La Serena',
            'carrera': 'Ingeniería Civil en Computación e Informática',
            'detalle': 'Coquimbo, Chile | Actualmente cursando 4° año',
        },
        'competencias': [
            'Trabajo en equipo', 'Comunicación efectiva', 'Apertura al aprendizaje',
            'Adaptabilidad', 'Responsabilidad',
        ],
        'idiomas': [
            {'idioma': 'Español', 'nivel': 'Nativo'},
            {'idioma': 'Inglés', 'nivel': 'Medio/Alto'},
        ],
    }
    return render(request, 'cv/cv_diego.html', contexto)

