from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
app_name = 'filme'
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filme/<int:pk>/', Detalhesfilmes.as_view(), name='detalhesfilmes'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('criar/', CriarConta.as_view(), name='criarconta')
]