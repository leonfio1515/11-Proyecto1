from django import forms

class Login(forms.Form):
    user = forms.CharField(max_length=50, verbose="Usuario")
    password = forms.PasswordInput(verbose="Contraseña")
