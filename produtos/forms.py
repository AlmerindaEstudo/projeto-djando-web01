
# produtos/forms.py
from django.forms import ModelForm
from .models import Produtos

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ["nome", "preco","descricao","quantidade","preco_compra","preco_venda","d_val"]
