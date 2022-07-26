import math
from django.db import models
from .usuario_cadastrado import UsuarioCadastrado


class Ficha(models.Model):
    """
    Modelo para uma ficha registrada no sistema
    """

    horario_entrada = models.DateTimeField(
        auto_now_add=True, verbose_name="Horário de Entrada")
    horario_saida = models.DateTimeField(
        verbose_name="Horário de Saída", null=True)
    usuario = models.ForeignKey(
        UsuarioCadastrado, blank=True, null=True, on_delete=models.PROTECT)
    pago = models.BooleanField(default=False)
    valor = models.FloatField(null=True, blank=True)

    @property
    def diff_horas(self):
        """
        Retorna quantas horas o usuário passou estacionado, arredondando para cima,
        ou None quando não existe horário de saída
        """
        if self.horario_saida:
            return math.ceil(((self.horario_saida - self.horario_entrada).seconds) / 3600)
        return None

    def __str__(self):
        return f'Ficha {self.id}'
