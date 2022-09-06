from django.shortcuts import render

def home(request):
    return render(request, 'events/home.html', {})

def about(request):
    return render(request, 'events/about.html', {})

def generate(request):
    return render(request, 'events/generate.html', {})