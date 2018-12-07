from django.db import models


class Participantes(models.Model):
    COD_PART = models.CharField(max_length=60, primary_key=True, null=False, blank=False)
    NOME = models.CharField(max_length=100, null=False, blank=False)
    COD_PAIS = models.CharField(max_length=5, null=False, blank=False)
    CNPJ = models.CharField(max_length=14)
    CPF = models.CharField(max_length=11)
    IE = models.CharField(max_length=14)
    COD_MUN = models.CharField(max_length=7)
    SUFRAMA = models.CharField(max_length=9)
    END = models.CharField(max_length=60, null=False, blank=False)
    NUM = models.CharField(max_length=10)
    COMPL = models.CharField(max_length=60)
    BAIRRO = models.CharField(max_length=60)
