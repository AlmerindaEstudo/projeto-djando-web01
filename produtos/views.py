# clientes/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produtos
from .forms import ProdutosForm



class ProdutosListView(ListView):
    model = Produtos
    template_name = "produtos/listap.html"
    context_object_name = "produtos"

class ProdutosCreateView(CreateView):
    model = Produtos
    form_class = ProdutosForm
    template_name = "produtos/formp.html"
    success_url = reverse_lazy("listap")



class ProdutosUpdateView(UpdateView):
    model = Produtos
    form_class = ProdutosForm
    template_name = "produtos/formp.html"
    success_url = reverse_lazy("listap")


class ProdutosDeleteView(DeleteView):
    model = Produtos
    template_name = "produtos/excluirp.html"
    success_url = reverse_lazy("listap")

