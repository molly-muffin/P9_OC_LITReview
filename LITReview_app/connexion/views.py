from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import forms


def logout_page(request):
	""" Déconnecter l'utilisateur et le rediriger vers la page de connexion. """
	logout(request)
	return redirect("login")


def login_page(request):
	""" L'utilisateur se connecte grâce à la fonction LoginForm. """
	form = forms.LoginForm()
	error_msg = ""
	if request.method == "POST":
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(
				username=form.cleaned_data["username"],
				password=form.cleaned_data["password"])
			if user is not None:
				login(request, user)
				return redirect("flux")
			else:
				error_msg = "Identifiant ou mot de passe invalide."
	return render(request,"login.html", context={"form": form, "error_msg": error_msg})


def signup_page(request):
	""" Permet à l'utilisateur de créer un compte et le redirige vers la page de flux. """
	form = forms.SignupForm()
	if request.method == "POST":
		form = forms.SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			# Connexion automatique de l'utilisateur à la page de flux.
			login(request, user)
			return redirect(settings.LOGIN_REDIRECT_URL)
	return render(request, "signup.html", context={"form": form})
