from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('generate', views.generate, name = 'generate'),
    path('events', views.all_event, name = 'list-events'),
]