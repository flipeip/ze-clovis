"""
Rotas de URL do sistema
"""
from django.urls import path
from .views import *

app_name = 'codigo'

urlpatterns = [
    path('admin/', AdminLogin.as_view()),
    path('entrada/', UserArrive.as_view()),
    path('saida/', UserDepart.as_view()),
]
