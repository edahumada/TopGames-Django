from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class ModificarPerfilForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput, min_length=6, max_length=18, label="Contraseña (Opcional)")
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput, label="Confirmar Contraseña (Opcional)")

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(ModificarPerfilForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'required': 'true'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'required': 'true'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['confirm_password'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


class ModificarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
