from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)
    codigo = models.CharField(max_length=6, unique=True, null=True, blank=True)
    carga_horaria = models.PositiveIntegerField(help_text="Em horas",null=False, blank=False)
    ementa = models.TextField(null=True, blank=True)
    ativa = models.BooleanField(default=True, null=False, blank=False)
    capacidade = models.IntegerField()
    criada_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    descricao = models.TextField(max_length=250,null=True, blank=True)

class Meta:
    ordering = ["nome"]

def __str__(self):
    return f"{self.codigo} – {self.nome}"