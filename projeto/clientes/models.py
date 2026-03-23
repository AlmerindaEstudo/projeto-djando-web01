from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Um model é uma classe em Python que representa uma tabela no banco de dados.
# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    idade= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)])
    
    def __str__(self):
       return self.nome