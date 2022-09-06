from django.shortcuts import render
from .models import Event

def home(request):
    return render(request, 'events/home.html', {})

def about(request):
    return render(request, 'events/about.html', {})

def generate(request):
    return render(request, 'events/generate.html', {})

def all_event(request):
    event_list = Event.objects.all()
    return render(request, 'events/generate.html', {'event_list':event_list})