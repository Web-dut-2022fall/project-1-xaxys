from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("/random", views.getRandomEntry, name="random"),
    path("/page/create", views.createPage, name="create"),
    path("entry/create", views.createEntry, name="createEntry"),
    path("entry/edit", views.editEntry, name="editEntry"),
    re_path(r'^wiki/(.+)/$', views.getEntry, name="entry"),
    re_path(r'^edit/(.+)/$', views.editPage, name="edit"),
]
