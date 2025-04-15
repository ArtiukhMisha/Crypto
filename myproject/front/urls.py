from django.contrib import admin
from django.urls import path, include
from .views import NaklonkiListView, NaklonkiDetailView

urlpatterns = [
    path("list/", NaklonkiListView.as_view(), name="naklonki-list"),
    path("list/my_deals/", NaklonkiListView.as_view(), name="naklonki-mylist"),
    path(
        "detail/<int:pk>/",
        NaklonkiDetailView.as_view(),
        name="naklonki-crud",
    ),
]
