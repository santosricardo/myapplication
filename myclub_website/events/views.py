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
        if 'submitted' in request.GET and 'submitted' is not NUL:
            submitted = True
        else:
            print('error!!!')
    return render(request, 'events/generate.html', {'form':form, 'submitted':submitted})

def all_quote(request):
    all_quotes = Event.objects.all()
    return render(request, 'events/all_quote.html', {'all_quotes':all_quotes})

# def add_event(request):
#     form = EventForm
#     return render(request, 'events/generate.html', {'form':form})