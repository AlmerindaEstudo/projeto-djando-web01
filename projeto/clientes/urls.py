from django.urls import path
from . import views 
from .views import(ClienteCreateView,ClienteDeleteView,ClienteListView,ClienteUpdateView)


urlpatterns = [
    path("",ClienteListView.as_view(),name="lista"),
    path("novo/",ClienteCreateView.as_view(),name="criar"),
    path("editar/<int:pk>/",ClienteUpdateView.as_view(),name="editar"),
    path("excluir/<int:pk>/",ClienteDeleteView.as_view(),name="excluir"),

]