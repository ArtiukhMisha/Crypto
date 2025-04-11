from django.contrib import admin
from django.urls import path, include
from .views import (
    NaklonkiListView,
    NaklonkiRetrieveUpdateDestroyView,
    MyDealsListView,
    NaklonkiCreateView,
)


urlpatterns = [
    path("list/", NaklonkiListView.as_view(), name="naklonki-list"),
    path("list/my_deals/", NaklonkiListView.as_view(), name="naklonki-list"),
    path(
        "detail/<int:pk>/",
        NaklonkiRetrieveUpdateDestroyView.as_view(),
        name="naklonki-crud",
    ),
    path("my_deals/", MyDealsListView.as_view({"get": "list"}), name="my-deals"),
    path("create/", NaklonkiCreateView.as_view(), name="naklonki-create"),
]
