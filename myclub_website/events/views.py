from tarfile import NUL
from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'events/home.html', {})

def about(request):
    return render(request, 'events/about.html', {})

def generate(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/generate?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/generate.html', {'form':form, 'submitted':submitted})

def all_quote(request):
    all_quote = Event.objects.all()
    return render(request, 'events/all_quote.html', {'all_quote':all_quote})

def show_quote(request, quote_id):
    quote = Event.objects.get(pk=quote_id)
    return render(request, 'events/show_quote.html', {'quote':quote})