from django.shortcuts import render
import rest_framework
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Naklonki
from .serilizers import NaklonkiSerializer

class NaklonkiListView(ListAPIView):
    queryset = Naklonki.objects.all()
    serializer_class = NaklonkiSerializer
    
