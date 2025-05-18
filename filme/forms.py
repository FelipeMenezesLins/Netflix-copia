from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario

class CriandoUsuario(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha'})
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
    }

class Emailenter(forms.Form):
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))