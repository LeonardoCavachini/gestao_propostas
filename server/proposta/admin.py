from django.contrib import admin
from .models import Proposta

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'endereco', 'valor', 'status')
    list_filter = ('status',)
