from django.views.generic.base import TemplateView
from django.contrib import messages
from django.shortcuts import redirect, reverse

from codigo.models import UsuarioCadastrado, Ficha


class UserArriveLogin(TemplateView):
    """
    Tela de entrada de identificação do usuário cadastrado
    """
    template_name = 'userArrive/login.html'

    def post(self, *args, **kwargs):
        """
        Procura o usuário e cria uma ficha nova
        """
        cpf = self.request.POST.get('cpf')
        if cpf:
            if UsuarioCadastrado.objects.filter(cpf=cpf).exists():
                usuario = UsuarioCadastrado.objects.get(cpf=cpf)
                if Ficha.objects.filter(usuario=usuario, pago=False).exists():
                    messages.error(
                        self.request, 'Existem fichas pendentes deste usuário')
                    return redirect(reverse('codigo:user-arrive'))
                ficha = Ficha(usuario=usuario)
                ficha.save()
                response = redirect(reverse('codigo:user-token'))
                response['Location'] += '?id=' + \
                    str(ficha.id) + '&nome=' + usuario.nome
                return response
            else:
                messages.error(self.request, 'Usuário não existe.')
        else:
            messages.error(self.request, 'CPF não informado.')
        return redirect(reverse('codigo:user-arrive'))
