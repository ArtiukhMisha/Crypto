from django.shortcuts import render
import rest_framework
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import generics

from .models import Naklonki
from .serilizers import NaklonkiSerializer


class NaklonkiListView(generics.ListAPIView):
    queryset = Naklonki.objects.all()
    serializer_class = NaklonkiSerializer

    def get(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        total = 0
        is_long = 0
        profit_if_1 = {
            "profit": 0,
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }
        profit_if_33 = {
            "profit": 0,
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }
        profit_if_50 = {
            "profit": 0,
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }
        profit_if_full = {
            "profit": 0,
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }
        stops = 0
        form_count = {
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }

        for i in data:
            form = i.get("form")
            form_count[form] += 1

            total += 1
            if i["is_long"]:
                is_long += 1
            if i["results"]["profit_if_1"] == -1 and i["results"]["profit_if_30"] == -1:
                stops += 1
            profit_if_1["profit"] += i["results"]["profit_if_1"]
            profit_if_33["profit"] += i["results"]["profit_if_30"]
            profit_if_50["profit"] += i["results"]["profit_if_50"]
            profit_if_full["profit"] += i["results"]["profit_if_full"]

            profit_if_1[i["form"]] += 1
            profit_if_33[i["form"]] += 1
            profit_if_50[i["form"]] += 1
            profit_if_full[i["form"]] += 1

        summary = {
            "long": is_long,
            "short": total - is_long,
            "profit_if_1": profit_if_1,
            "profit_if_33": profit_if_33,
            "profit_if_50": profit_if_50,
            "profit_if_full": profit_if_full,
            "form_count": form_count,
        }
        response_data = {
            "results": data,
            "summary": summary,
        }

        return Response(response_data)


class NaklonkiRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Naklonki.objects.all()
    serializer_class = NaklonkiSerializer
