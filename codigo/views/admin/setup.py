from django.views.generic.base import TemplateView
from django.shortcuts import redirect, reverse

from codigo.models import Config, Ficha


class AdminSetup(TemplateView):
    """
    Tela de configurações globais do sistema
    """
    template_name = 'login/setup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config = Config.get_instance()
        context['preco'] = config.preco
        context['vagas'] = config.vagas
        context['desconto'] = config.desconto
        context['estacionados'] = Ficha.objects.filter(pago=False).count()
        return context

    def post(self, *args, **kwargs):
        config = Config.get_instance()
        if self.request.POST.get('novoValorHora'):
            config.preco = float(self.request.POST.get('novoValorHora'))
        if self.request.POST.get('novoNumeroVagas'):
            config.vagas = int(self.request.POST.get('novoNumeroVagas'))
        if self.request.POST.get('novoValorDesconto'):
            config.desconto = int(self.request.POST.get('novoValorDesconto'))
        config.save()
        return redirect(reverse('codigo:admin-config'))
