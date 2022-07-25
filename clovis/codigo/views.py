"""
Lógica do backend do sistema
"""

from django.contrib import messages
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, reverse

from .models import Admin, UsuarioCadastrado, Ficha, Config


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config = Config.get_singleton()
        context['preco'] = config.preco
        context['vagas'] = config.vagas
        context['desconto'] = config.desconto
        context['estacionados'] = Ficha.objects.filter(pago=False).count()
        return context
    
    def post(self, *args, **kwargs):
        config = Config.get_singleton()
        if self.request.POST.get('novoValorHora'):
            config.preco = float(self.request.POST.get('novoValorHora'))
        if self.request.POST.get('novoNumeroVagas'):
            config.vagas = int(self.request.POST.get('novoNumeroVagas'))
        if self.request.POST.get('novoValorDesconto'):
            config.desconto = int(self.request.POST.get('novoValorDesconto'))
        config.save()
        return redirect(reverse('codigo:admin-config'))

class AdminUserRegister(TemplateView):
    """
    Tela de cadastro de usuários
    """
    template_name = 'login/user-register.html'

    def post(self, *args, **kwargs):
        if self.request.POST.get('userName') and self.request.POST.get('cpf'):
            usuario = UsuarioCadastrado()
            usuario.nome = self.request.POST.get('userName')
            usuario.cpf = self.request.POST.get('cpf')
            usuario.save()
            return redirect(reverse('codigo:admin-home'))
        message()
        return redirect(reverse('codigo:admin-user-register'))

class AdminLog(TemplateView):
    """
    Tela de log de fichas
    """

    template_name = 'login/token-log.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estacionados'] = Ficha.objects.filter()
        return context

class UserArrive(TemplateView):
    """
    Tela inicial na chegada do usuário
    """
    template_name = 'userArrive/entrada.html'

    def post(self, *args, **kwargs):
        ficha = Ficha()
        ficha.save()
        response = redirect(reverse('codigo:user-token'))
        response['Location'] += '?id=' + str(ficha.id)
        return response


class UserArriveLogin(TemplateView):
    """
    Tela de entrada de identificação do usuário cadastrado
    """
    template_name = 'userArrive/login.html'

    def post(self, *args, **kwargs):
        cpf = self.request.POST.get('cpf')
        if cpf:
            if UsuarioCadastrado.objects.filter(cpf=cpf).exists():
                usuario = UsuarioCadastrado.objects.get(cpf = cpf)
                if Ficha.objects.filter(usuario = usuario, pago = False).exists():
                    return redirect(reverse('codigo:user-arrive'))
                ficha = Ficha(usuario = usuario)
                ficha.save()
                response = redirect(reverse('codigo:user-token'))
                response['Location'] += '?id=' + str(ficha.id) + '&nome=' + usuario.nome
                return response
        return redirect(reverse('codigo:user-arrive'))


class UserArriveToken(TemplateView):
    """
    Tela de exibição da ficha do usuário
    """
    template_name = 'userArrive/token.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.request.GET.get('id')
        if self.request.GET.get('nome'):
            context['nome'] = self.request.GET.get('nome')
        return context


class UserDepart(TemplateView):
    """
    Tela inicial na saída do usuário
    """
    template_name = 'userDepart/saida.html'

    def post(self, *args, **kwargs):
        if self.request.POST.get('ficha'):
            if Ficha.objects.filter(id = int(self.request.POST.get('ficha'))).exists():
                ficha = Ficha.objects.get(id = int(self.request.POST.get('ficha')))
                if not ficha.pago:
                    ficha.horario_saida = timezone.now()
                    response = redirect(reverse('codigo:user-price'))
                    preco = ficha.diff_horas * Config.get_singleton().preco
                    if ficha.usuario:
                        preco -= ((preco * Config.get_singleton().desconto) / 100)
                    response['Location'] += '?preco=' + '{:.2f}'.format(preco)
                    ficha.valor = preco
                    ficha.pago = True
                    ficha.save()
                    return response
                else:
                    messages.error(self.request, 'Ficha já paga')
            else:
                messages.error(self.request, 'Ficha não existente')
        else:
            messages.error(self.request,'Ficha não informada')
        return redirect(reverse('codigo:user-depart'))


class UserDepartPrice(TemplateView):
    """
    Tela de exibição de preço da estadia do usuário
    """
    
    template_name = 'userDepart/price.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preco'] = (self.request.GET.get('preco')).replace('.', ',')
        return context