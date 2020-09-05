from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("edit/<str:title>", views.edit_page, name="edit"),
    path("random", views.random_page, name="random"),
    path("search", views.search, name="search"),
    path("add", views.add_page, name="add"),


]
