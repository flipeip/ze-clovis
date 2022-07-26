from django.views.generic.base import TemplateView


class UserDepartPrice(TemplateView):
    """
    Tela de exibição de preço da estadia do usuário
    """
    
    template_name = 'userDepart/price.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preco'] = (self.request.GET.get('preco')).replace('.', ',')
        return context