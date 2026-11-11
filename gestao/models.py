from django.db import models


class Disciplina(models.Model):
    codigo = models.CharField(max_length=6, null=True, blank=True)
    nome = models.CharField(max_length=120, null=False, blank=False)
    carga_horaria = models.IntegerField(null = False, blank=False)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    capacidade = models.IntegerField()
    ativa = models.BooleanField(default=True, null=False, blank=False)
    
