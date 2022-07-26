from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import redirect, reverse

from codigo.models import Admin


class AdminLogin(TemplateView):
    """
    Tela de login do administrador do sistema
    """
    template_name = 'login/login.html'

    def post(self, *args, **kwargs):
        """
        Validação do formulário, busca do usuário e confirmação da senha
        """

        email = self.request.POST.get('email')
        senha = self.request.POST.get('password')

        if email:
            if Admin.objects.filter(email=email).exists():
                admin = Admin.objects.get(email=email)
                if admin.senha == senha:
                    return redirect(reverse('codigo:admin-home'))
                messages.error(
                    self.request, 'Senha não corresponde à conta do administrador')
            else:
                messages.error(
                    self.request, 'Conta de administrador não existe')
        else:
            messages.error(self.request, 'E-mail não informado')
        return redirect(reverse('codigo:admin-login'))
