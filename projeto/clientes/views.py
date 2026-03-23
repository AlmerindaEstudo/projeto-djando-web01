from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Clientes
from .forms import ClienteForm

#A view serve para receber a requisição do usuário, processar a lógica da aplicação e retornar uma resposta.

#👉 Ela decide o que fazer e o que mostrar.
# Create your views here.


#model = Cliente → define qual tabela do banco a view usa
#template_name → define qual HTML será exibido
#context_object_name → nome da variável usada no template
#form_class = ClienteForm → define qual formulário será usado para criar/editar/validar dados
#success_url = reverse_lazy("lista") Define para onde o usuário será redirecionado após uma ação bem-sucedida

class ClienteListView(ListView):
    model= Clientes
    template_name = "clientes/lista.html"
    context_object_name = "clientes"

class ClienteCreateView(CreateView):
    model= Clientes
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("lista")

class ClienteUpdateView(UpdateView):
    model= Clientes
    form_Class= ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("lista")

class ClienteDeleteView(DeleteView):
    model= Clientes
    template_name = "clientes/excluir.html"
    success_url = reverse_lazy("lista")
