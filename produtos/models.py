# Create your models here.
#  - crie um novo app chamado produtos e configure o CRUD para um modelo Produto com os campos nome, preço e descrição, 
#quantidade, preco de compra, preco de venda, data de validade, os campos nome e preço devem ser obrigatórios.
from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao=models.CharField(max_length=100,blank=True, null=True)
    quantidade=models.IntegerField(blank=True, null=True)
    preco_compra=models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda=models.DecimalField(max_digits=10, decimal_places=2)
    d_val=models.DateField(blank=True, null=True)


    def __str__(self):
        return self.nome
