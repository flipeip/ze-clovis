"""
Módulo para modelos do banco de dados relacionados ao dono de um veículo
"""

from django.db import models


class Dono(models.Model):
    """
    Classe modelo para o dono de veículo cadastrado no sistema
    """

    cpf = models.CharField(max_length=11, null=False,
                           blank=False, primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
