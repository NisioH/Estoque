from django.contrib import admin
from django.urls import path, include
from mercadorias.views import listar_mercadorias
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", listar_mercadorias, name="home"),
    path("", include("mercadorias.urls")),
]

