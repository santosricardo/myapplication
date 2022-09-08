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

def all_event(request):
    event_list = Event.objects.all()
    return render(request, 'events/generate.html', {'event_list':event_list})

# def add_event(request):
#     form = EventForm
#     return render(request, 'events/generate.html', {'form':form})