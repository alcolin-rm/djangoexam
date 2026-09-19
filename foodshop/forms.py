from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Order


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Client
        fields = ('username', 'email')


class OrderForm(forms.ModelForm):
    use_bonuses = forms.BooleanField(
        required=False,
        label='Списать бонусы'
    )

    class Meta:
        model = Order
        fields = ('dish',)