from django.urls import path
# Desde este paquete vamos a importar el archivo views
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="index"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="Results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="Vote"),
]
