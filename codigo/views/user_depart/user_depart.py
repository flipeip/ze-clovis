from django.views.generic.base import TemplateView
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, reverse

from codigo.models import Ficha, Config


class UserDepart(TemplateView):
    """
    Tela inicial na saída do usuário
    """
    template_name = 'userDepart/saida.html'

    def post(self, *args, **kwargs):
        """
        Fecha a ficha, calcula o preço e 'paga'
        """
        if self.request.POST.get('ficha'):
            if Ficha.objects.filter(id=int(self.request.POST.get('ficha'))).exists():
                ficha = Ficha.objects.get(
                    id=int(self.request.POST.get('ficha')))
                if not ficha.pago:
                    ficha.horario_saida = timezone.now()
                    response = redirect(reverse('codigo:user-price'))
                    preco = ficha.diff_horas * Config.get_instance().preco
                    if ficha.usuario:
                        preco -= ((preco * Config.get_instance().desconto) / 100)
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
            messages.error(self.request, 'Ficha não informada')
        return redirect(reverse('codigo:user-depart'))
