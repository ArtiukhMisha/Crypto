from django.contrib import admin
from django.urls import path, include
from .views import (
    NaklonkiListView,
    NaklonkiRetrieveUpdateDestroyView,
    MyDealsListView,
    NaklonkiCreateView,
)
from rest_framework.authtoken import views


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
    path("api-token-auth/", views.obtain_auth_token, name="api-token-auth"),
]
