from django.views.generic.base import TemplateView

from codigo.models import Ficha


class AdminLog(TemplateView):
    """
    Tela de log de fichas
    """

    template_name = 'login/token-log.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estacionados'] = Ficha.objects.all().order_by('-id')
        return context