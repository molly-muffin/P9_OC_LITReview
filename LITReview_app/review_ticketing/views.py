from .models import Band
from django.shortcuts import render


def hello(request):
    bands = Band.objects.all()
    return render(request, 'flux.html')