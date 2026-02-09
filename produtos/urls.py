

# clientes/urls.py
from django.urls import path
from .views import (
    ProdutosListView,
    ProdutosCreateView,
    ProdutosUpdateView,
    ProdutosDeleteView
)

urlpatterns = [
    path("listap", ProdutosListView.as_view(), name="listap"),
    path("novop/", ProdutosCreateView.as_view(), name="criarp"),
    path("editarp/<int:pk>/", ProdutosUpdateView.as_view(), name="editarp"),
    path("excluirp/<int:pk>/", ProdutosDeleteView.as_view(), name="excluirp"),
]

