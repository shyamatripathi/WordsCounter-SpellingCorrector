from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the home page
    path('counter', views.counter, name='counter'),  # URL for the word counter page
]
