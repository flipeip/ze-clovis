from django.views.generic.base import TemplateView


class AdminHome(TemplateView):
    """
    Tela inicial do administrador do sistema
    """
    template_name = 'login/home.html'