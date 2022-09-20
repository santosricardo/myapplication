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
    form = EventForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.due_back = form.cleaned_data['description']
            form.save()
            return HttpResponseRedirect('/generate')
            #return HttpResponseRedirect('/show_quotes/')
    return render(request, 'events/generate.html', {'form':form})

def all_quote(request):
    all_quote = Event.objects.all()
    return render(request, 'events/all_quote.html', {'all_quote':all_quote})

def show_quote(request, quote_id):
    quote = Event.objects.get(pk=quote_id)
    #answer = Event.save_image(quote)
    Event.save_image(quote)
    return render(request, 'events/show_quote.html', {'quote':quote})