from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('description',)
        labels = {'description':''}
        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the quotes here','rows':'1'})
        }
