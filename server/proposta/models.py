from django.db import models

# Create your models here.
class Proposta(models.Model):
    nome = models.CharField(
        verbose_name=('Nome Completo'),
        null=True,
        max_length=40
    )
    cpf = models.CharField(
        verbose_name=('CPF'),
        max_length=14,
        null=True,
    )
    endereco = models.CharField(
        verbose_name=('Endereço'),
        null=True,
        max_length=60
    )
    valor = models.FloatField(
        verbose_name=('Valor Emprestimo'),
        null=True,
    )
    status = models.CharField(
        verbose_name=('Status'),
        null=True,
        blank=True,
        max_length=10
    )

    def __str__(self):
        return self.nome