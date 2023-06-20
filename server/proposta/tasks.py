from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import Proposta

@shared_task
def analisar():
  lista = Proposta.objects.all()
  for i in lista:
    if i.valor > 80:
       i.status = "Negado"
       i.save()
    else:
      i.status = 'Aprovado'
      i.save()