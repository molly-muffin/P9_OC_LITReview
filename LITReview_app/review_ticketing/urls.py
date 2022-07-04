from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import hello as flux

urlpatterns = [
	path("flux/", flux, name="flux"),
]
if settings.DEBUG:
	urlpatterns += static(
		settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
