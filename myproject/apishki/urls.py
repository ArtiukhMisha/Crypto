from django.contrib import admin
from django.urls import path, include
from .views import NaklonkiListView 



urlpatterns = [
    path('list/', NaklonkiListView.as_view(), name='naklonki-list'),
    
]
