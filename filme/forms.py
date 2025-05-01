from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario

class CriandoUsuario(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

class Emailenter(forms.Form):
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))