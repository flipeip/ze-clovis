"""
Lógica do backend do sistema
"""

from django.views.generic.base import TemplateView
from django.shortcuts import redirect, reverse

from .models import Admin


class AdminLogin(TemplateView):
    """
    Tela de login do administrador do sistema
    """
    template_name = 'login/login.html'

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        senha = self.request.POST.get('password')

        if email:
            admin = Admin.objects.get(email=email)
            if admin.senha == senha:
                return redirect(reverse('codigo:admin-home'))
        return redirect(reverse('codigo:admin-login'))


class AdminHome(TemplateView):
    """
    Tela inicial do administrador do sistema
    """
    template_name = 'login/home.html'


class AdminSetup(TemplateView):
    """
    Tela de configurações globais do sistema
    """
    template_name = 'login/setup.html'


class AdminUserRegister(TemplateView):
    """
    Tela de cadstro de usuários
    """
    template_name = 'login/user-register.html'


class UserArrive(TemplateView):
    """
    Tela inicial na chegada do usuário
    """
    template_name = 'userArrive/entrada.html'


class UserArriveLogin(TemplateView):
    """
    Tela de entrada de identificação do usuário cadastrado
    """
    template_name = 'userArrive/login.html'


class UserArriveToken(TemplateView):
    """
    Tela de exibição da ficha do usuário
    """
    template_name = 'userArrive/token.html'


class UserDepart(TemplateView):
    """
    Tela inicial na saída do usuário
    """
    template_name = 'userDepart/saida.html'


class UserDepartPrice(TemplateView):
    """
    Tela de exibição de preço da estadia do usuário
    """
    template_name = 'userDepart/price.html'
