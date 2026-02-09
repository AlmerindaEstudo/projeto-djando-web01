

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone=models.IntegerField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome
