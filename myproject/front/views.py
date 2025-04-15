import json
import sys
import requests
from django.shortcuts import render, redirect
from django.urls import reverse

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from apishki.models import Naklonki
from django.conf import settings


class NaklonkiListView(TemplateView):
    template_name = "front/list.html"
    context_object_name = "naklonki"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and self.request.GET.get(
            "my_deals", False
        ):
            return redirect("/login/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)

        # Fetch API data
        my_deals = self.request.GET.get("my_deals", False)
        print(my_deals)  # Debugging line to check the value of my_deals
        if my_deals:
            api_url = f"{settings.API_BASE_URL}/list/my_deals"
        else:
            api_url = f"{settings.API_BASE_URL}/list/"
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad status codes
            api_data = response.json()  # Parse the JSON response
        except requests.exceptions.RequestException as e:
            api_data = {"error": str(e)}  # Handle API errors gracefully

        # Add API data to the context

        context["api_data"] = api_data
        print(context)  # Debugging line to check API data
        return context


class NaklonkiDetailView(TemplateView):
    template_name = "front/detail.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_url = f"{settings.API_BASE_URL}/detail/<int:pk>/"

        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad status codes
            api_data = response.json()  # Parse the JSON response
        except requests.exceptions.RequestException as e:
            pass  ######################################

        print(api_data)
        context["api_data"] = api_data

        return context
