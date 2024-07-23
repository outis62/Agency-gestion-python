from django import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('login', login_view, name="login"),
    path('register', register, name="register"),
    path('welcome/', welcome, name='welcome'),
    path('deconnexion/', deconnexion, name='deconnexion'),
]
