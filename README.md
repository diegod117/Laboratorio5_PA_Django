# Laboratorio 5 – Django: Sitio de CVs en equipo

Programación de Aplicaciones — Unidad III — Laboratorio 5

Proyecto Django (`sitio_cv`) donde cada integrante del grupo construye su propia página de CV, trabajando en equipo con Git (ramas, commits y Pull Requests).

## Requisitos

- **Python 3.10+** (todo el trabajo se desarrolla en Python)
- **Django** (`pip install django`)
- Git

## Puesta en marcha

```bash
git clone <url-del-repositorio>
cd Laboratorio5_PA_Django
python -m venv venv
venv\Scripts\activate        # Windows
pip install django
python manage.py runserver
```

Luego abrir <http://127.0.0.1:8000/>.

## Pasos del laboratorio

### Paso 1 — Crear el proyecto y la app
- `django-admin startproject sitio_cv`
- Dentro del proyecto: `python manage.py startapp cv`
- Registrar `"cv"` en `INSTALLED_APPS` (`settings.py`) y confirmar que `python manage.py runserver` funciona.
- Commit, Pull Request a `main`, revisión y aprobación del grupo antes del paso 2.

### Paso 2 — Plantilla base y página de inicio
- Crear carpeta `templates/` en la raíz y agregarla a `DIRS` en `TEMPLATES` (`settings.py`).
- Crear `base.html` con encabezado, navegación y pie comunes, con `{% block content %}{% endblock %}`.
- Crear la vista `home` en `views.py` que renderiza `home.html` (extiende `base.html`) con los nombres de los integrantes, cada uno como enlace a su CV.
- Conectar `home` en `urls.py` en la ruta raíz.
- Commit y Pull Request a `main`.

### Paso 3 — CV de ejemplo (en equipo)
- La vista de ejemplo arma un diccionario de contexto (nombre, título profesional, contacto, habilidades, experiencia) y llama a `render(request, 'cv/cv_ejemplo.html', contexto)`.
- `cv_ejemplo.html` extiende `base.html`, usa `{{ variable }}` para datos simples y `{% for %}` para las listas.
- Commit y Pull Request a `main`.

### Paso 4 — CV individual
- Hacer pull de `main`.
- Cada integrante crea su rama desde `main` (ej. `cv-nombre`).
- Agrega su vista en `views.py` (ej. `cv_nombre`) con su contexto, su template (ej. `cv_nombre.html`), su ruta en `urls.py` (ej. `/cv/nombre/`) y su enlace en `home.html`.
- Probar la página en el navegador.
- Mínimo **3 commits incrementales** y push de la rama.

### Paso 5 — Pull Request, merge y cierre
- Cada integrante abre un Pull Request de su rama a `main`.
- La persona anfitriona revisa y hace merge uno por uno, verificando que el servidor siga funcionando.
- Los conflictos en `home.html` son esperables: resolverlos conservando los enlaces de todos.
- Navegar el sitio completo y verificar el acceso al CV de cada integrante.
- Crear el documento Word `Evidencia_Laboratorio5_NombreDelGrupo` con capturas de la página de inicio y del CV de cada integrante.

## Estructura esperada

```
Laboratorio5_PA_Django/
├── manage.py
├── sitio_cv/        # configuración (settings.py, urls.py)
├── cv/              # app (views.py, ...)
└── templates/
    ├── base.html
    ├── home.html
    └── cv/
        ├── cv_ejemplo.html
        └── cv_nombre.html
```

## Flujo de trabajo con Git

- Nunca trabajar directo en `main`: usar ramas y Pull Requests.
- Commits pequeños y descriptivos.

## Integrantes

- _Agregar nombres del grupo_
