from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/ejemplo/', views.cv_ejemplo, name='cv_ejemplo'),
    # Cada integrante agrega aquí su ruta, ej:
    path('cv/johann/', views.cv_johann, name='cv_johann'),
    # path('cv/nombre/', views.cv_nombre, name='cv_nombre'),
]
