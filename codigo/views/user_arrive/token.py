from django.views.generic.base import TemplateView


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