"""
Rotas de URL do sistema
"""
from django.urls import path
from .views import *

app_name = 'codigo'

urlpatterns = [
    path('', AdminLogin.as_view(), name='admin-login'),
    path('home/', AdminHome.as_view(), name='admin-home'),
    path('configuracao/', AdminSetup.as_view(), name='admin-config'),
    path('registro/', AdminUserRegister.as_view(), name='admin-user-register'),

    path('entrada/', UserArrive.as_view(), name='user-arrive'),
    path('entrada/login', UserArriveLogin.as_view(), name='user-login'),
    path('entrada/ficha', UserArriveToken.as_view(), name='user-token'),

    path('saida/', UserDepart.as_view(), name='user-depart'),
    path('saida/pagamento', UserDepartPrice.as_view(), name='user-price'),
]
