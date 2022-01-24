from django.urls import path
# Desde este paquete vamos a importar el archivo views
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
