from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
# Create your views here.

class Homepage(FormView):
    template_name = 'home.html'
    form_class = Emailenter

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email = email)
        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        perguntas = Pergunta.objects.all()  # parênteses aqui!
        context['object_list'] = perguntas  # cuidado com o nome da chave
        return context


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'filmes.html'
    model = Filme 

class Detalhesfilmes(LoginRequiredMixin, DetailView):
    template_name = 'episodios.html'
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:3]
        context['relacionados'] = filmes_relacionados
        return context 

class CriarConta(FormView):
    template_name = 'criar.html'
    form_class = CriandoUsuario

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse('filme:login')