from django.shortcuts import render
from .models import Burgers, Stuffed_berger


def index(request):
    burgers = Burgers.objects.all()
    stuffed_berger = Stuffed_berger.objects.all()
    context = {
        'burgers': burgers,
        'stuffed_berger': stuffed_berger
    }
    return render(request, 'index.html', context)
