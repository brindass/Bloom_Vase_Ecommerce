from django.urls import path
from .views import test, register, user_login, home, user_logout

urlpatterns =[
    # path('',home,name='home'),
    path('register/',register,name = 'register'),
    path('login/',user_login,name='user_login'),
    path('logout/',user_logout,name='user_logout')
]
    