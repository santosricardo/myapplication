from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('generate', views.generate, name='generate'),
    path('quotes', views.all_quote, name='all_quote'),
    path('show_quotes/<quote_id>', views.show_quote, name='show_quote'),
]