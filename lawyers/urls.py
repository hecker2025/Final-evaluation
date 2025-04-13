from django.urls import path
from . import views

urlpatterns = [path('lawyers/', views.lawyers, name = 'lawyers'),
               ]