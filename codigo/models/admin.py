from django.db import models


class Admin(models.Model):
    """
    Modelo para administrador do sistema
    """

    email = models.EmailField()
    senha = models.CharField(max_length=32)

    def __str__(self):
        return f'Admin {self.email}'