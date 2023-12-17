from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100)
    codigo_produto = models.IntegerField()
    descricao_produto = models.CharField(max_length=100)
    preco_produto = models.FloatField()