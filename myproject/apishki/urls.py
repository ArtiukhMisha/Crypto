from django.contrib import admin
from django.urls import path, include
from .views import NaklonkiListView, NaklonkiRetrieveUpdateDestroyView


urlpatterns = [
    path("list/", NaklonkiListView.as_view(), name="naklonki-list"),
    path(
        "detail/<int:pk>/",
        NaklonkiRetrieveUpdateDestroyView.as_view(),
        name="naklonki-crud",
    ),
]
