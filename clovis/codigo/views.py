"""
Lógica do backend do sistema
"""

from django.views.generic.base import TemplateView


class AdminLogin(TemplateView):
    """
    Tela de login do administrador do sistema
    """
    template_name = 'admin/login.html'


class UserArrive(TemplateView):
    """
    Tela inicial na chegada do usuário
    """
    template_name = 'userArrive/entrada.html'


class UserDepart(TemplateView):
    """
    Tela inicial na saída do usuário
    """
    template_name = 'userDepart/saida.html'
