from django.db import models


class UsuarioCadastrado(models.Model):
    """
    Modelo para usuário cadastrado no sistema
    """

    cpf = models.CharField(max_length=11, null=False,
                           blank=False, primary_key=True, verbose_name="CPF")
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.nome} ({self.cpf})'
