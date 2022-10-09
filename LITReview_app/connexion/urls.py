from django.urls import path
from .views import login_page, logout_page, signup_page, admin_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
	path("admin/", admin_page, name="admin"),
	path("signup/", signup_page, name="signup"),
	path("", login_page, name="login"),
	path("logout/", logout_page, name="logout"),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)