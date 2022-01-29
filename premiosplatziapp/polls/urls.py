from django.urls import path
# Desde este paquete vamos a importar el archivo views
from . import views

# url + app_name + name
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/detail/estaeslamejorpagina", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:pk>/vote/", views.vote, name="vote"),
]
