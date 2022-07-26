from django.views.generic.base import TemplateView
from django.shortcuts import redirect, reverse

from codigo.models import Ficha


class UserArrive(TemplateView):
    """
    Tela inicial na chegada do usuário
    """
    template_name = 'userArrive/entrada.html'

    def post(self, *args, **kwargs):
        """
        Cria uma nova ficha
        """
        ficha = Ficha()
        ficha.save()
        response = redirect(reverse('codigo:user-token'))
        response['Location'] += '?id=' + str(ficha.id)
        return response
