from django.urls import path
from .views import login_page, logout_page, signup_page


urlpatterns = [
	path("signup/", signup_page, name="signup"),
	path("", login_page, name="login"),
	path("logout/", logout_page, name="logout"),
]