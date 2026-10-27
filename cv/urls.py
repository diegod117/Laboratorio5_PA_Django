from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/ejemplo/', views.cv_ejemplo, name='cv_ejemplo'),
    path('cv/diego/', views.cv_diego, name='cv_diego'),
    # Cada integrante agrega aquí su ruta, ej:
    # path('cv/nombre/', views.cv_nombre, name='cv_nombre'),
]
