from django.contrib import admin
from django.urls import path, include
from .views import (
    NaklonkiListView,
    NaklonkiRetrieveUpdateDestroyView,
    NaklonkiCreateView,
)
from rest_framework.authtoken import views


urlpatterns = [
    path("list/", NaklonkiListView.as_view(), name="api-naklonki-list"),
    path("list/my_deals/", NaklonkiListView.as_view(), name="api-naklonki-mylist"),
    path(
        "detail/<int:pk>/",
        NaklonkiRetrieveUpdateDestroyView.as_view(),
        name="api-naklonki-crud",
    ),
    path("create/", NaklonkiCreateView.as_view(), name="api-naklonki-create"),
    path("api-token-auth/", views.obtain_auth_token, name="api-api-token-auth"),
]
