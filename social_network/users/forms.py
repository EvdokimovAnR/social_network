from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес электронной почты'}))
    age = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваш возраст(необязательно)'}))
    country = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите вашу страну(необязательно)'}))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваш город(необязательно)'}))
    telephone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваш номер телефона(необязательно)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'age', 'country', 'city', 'telephone_number', 'password1', 'password2')

