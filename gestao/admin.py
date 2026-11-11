from django.contrib import admin
from gestao.models import Disciplina

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'carga_horaria', 'capacidade', 'ativa']
    search_fields = ['codigo', 'nome']
    list_filter = ['ativa']
    list_editable = ['ativa']
    list_per_page = 20
readonly_fields = ['criada_em']
fieldsets = [
    ('Identificação', {'fields': ['codigo', 'nome', 'capacidade']}),
    ('Conteúdo', {'fields': ['carga_horaria', 'ementa']}),
    ('Situação', {'fields': ['ativa', 'criada_em']}),
]   
actions = ['desativar']    

@admin.action(description="Desativar selecionadas")    
def desativar(self, request, queryset):
    queryset.update(ativa=False)