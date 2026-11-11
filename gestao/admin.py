from django.contrib import admin
from gestao.models import Disciplina

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'carga_horaria', 'capacidade', 'ativa']
