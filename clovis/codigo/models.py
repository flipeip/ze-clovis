"""
Arquivo de modelos do banco de dados seguindo o padrão do django
"""

from django.db import models


class Config(models.Model):
    """
    Modelo para configurações globais do sistema

    Obs.: Segue o padrão Singleton
    """
    preco = models.FloatField(verbose_name="Preço por Hora")
    vagas = models.PositiveIntegerField(verbose_name="Número de Vagas")

    def get_singleton():
        if not Config.objects.first():
            Config(preco=10.00, vagas=50).save()
        return Config.objects.first()


class Admin(models.Model):
    """
    Modelo para administrador do sistema
    """

    email = models.EmailField()
    senha = models.CharField(max_length=32)


class UsuarioCadastrado(models.Model):
    """
    Modelo para usuário cadastrado no sistema
    """

    cpf = models.CharField(max_length=11, null=False,
                           blank=False, primary_key=True, verbose_name="CPF")
    nome = models.CharField(max_length=50, null=False, blank=False)


class Ficha(models.Model):
    """
    Modelo para uma ficha registrada no sistema
    """

    horario_entrada = models.DateTimeField(
        auto_now_add=True, verbose_name="Horário de Entrada")
    horario_saida = models.DateTimeField(verbose_name="Horário de Saída", null=True)
    usuario = models.ForeignKey(
        UsuarioCadastrado, blank=True, null=True, on_delete=models.PROTECT)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f'Ficha {self.id}';
