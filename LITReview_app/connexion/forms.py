from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
	""" Formulaire de création d'un compte utilisateur grâce au nom d'utilisateur et au mot de passe. """
	username = forms.CharField(
		max_length=64,
		widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}),
		label="Nom d’utilisateur")
	password1 = forms.CharField(
		max_length=64,
		widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}),
		label="Mot de passe")
	password2 = forms.CharField(
		max_length=64,
		widget=forms.PasswordInput(attrs={"placeholder": "Confirmer mot de passe"}),
		label="Mot de passe")


class LoginForm(forms.Form):
	"""	Form for user can login, thanks username and password. """
	username = forms.CharField(
		max_length=64,
		widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}),
		label="Nom d’utilisateur")
	password = forms.CharField(
		max_length=64,
		widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}),
		label="Mot de passe")
