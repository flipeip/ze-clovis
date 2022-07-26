from django.db import models

class Config(models.Model):
    """
    Modelo para configurações globais do sistema
    
    Obs.: Utilize get_instance() para pegar as configurações globais
    do app (padrão Singleton)
    """

    preco = models.FloatField(null=False, blank=False)
    desconto = models.PositiveIntegerField(null=False, blank=False, default=30)
    vagas = models.PositiveIntegerField(null=False, blank=False)

    def get_instance():
        if not Config.objects.first():
            Config(preco=10.00, vagas=50, desconto=30).save()
        return Config.objects.first()
    
    def __str__(self):
        return f'Configurações do Sistema'
