from django.urls import path

# importar las vistas
from . import views

urlpatterns = [
    path('', views.hello)
]
