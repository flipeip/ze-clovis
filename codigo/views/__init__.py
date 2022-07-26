"""
Módulo de views: consiste em toda a lógica de backend das páginas
"""

from .admin.login import AdminLogin
from .admin.home import AdminHome
from .admin.setup import AdminSetup
from .admin.log import AdminLog
from .admin.user_register import AdminUserRegister

from .user_arrive.user_arrive import UserArrive
from .user_arrive.login import UserArriveLogin
from .user_arrive.token import UserArriveToken

from .user_depart.user_depart import UserDepart
from .user_depart.price import UserDepartPrice