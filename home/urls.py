
from django.urls import path
from . import views 
from .views import HomeView


urlpatterns = [
    path('', HomeView, name='home'),
]