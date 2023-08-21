from django.urls import path

from .  import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre", views.sobre, name="sobre"),
    path("equipe", views.equipe, name="equipe")
    path("campanhas", views.campanhas, name="campanhas")
]