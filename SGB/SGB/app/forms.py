from django import forms
from .models import User, Bem
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm



UserModel = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(
        label='Tipo de cargo:',
        choices=(
            ('colaborador', 'Colaborador'),
            ('gerente', 'Gerente'),
        ),
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('As senhas não coincidem.')

        return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)



class BemForm(forms.ModelForm):
    class Meta:
        model = Bem
        fields = ('objeto', 'codigo', 'data_adesao', 'local_utilizacao')

class AlteracaoBemForm(forms.Form):
      codigo = forms.CharField(max_length=50)
      novo_local = forms.CharField(max_length=100)


