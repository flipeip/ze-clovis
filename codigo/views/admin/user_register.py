from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import redirect, reverse

from codigo.models import UsuarioCadastrado


class AdminUserRegister(TemplateView):
    """
    Tela de cadastro de usuários
    """
    template_name = 'login/user-register.html'

    def post(self, *args, **kwargs):
        if (self.request.POST.get('userName') != '') and (self.request.POST.get('cpf') != ''):
            if not (UsuarioCadastrado.objects.filter(cpf=self.request.POST.get('cpf')).exists()):
                usuario = UsuarioCadastrado()
                usuario.nome = self.request.POST.get('userName')
                usuario.cpf = self.request.POST.get('cpf')
                usuario.save()
                return redirect(reverse('codigo:admin-home'))
            else:
                messages.error(self.request, 'CPF já cadastrado')
        else:
            messages.error(self.request, 'Informe todos os dados do usuário')
        return redirect(reverse('codigo:admin-user-register'))
