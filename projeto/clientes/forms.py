#✔ Gera HTML
#✔ Conecta com o model
#✔ Converte dados corretamente


from django.forms import ModelForm
from .models import Clientes


class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ["nome","idade"]