from django.shortcuts import render, redirect
import rest_framework
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import generics

from .models import Naklonki
from .serilizers import NaklonkiSerializer
from .permission import IsOwnerOrMentorOrReadOnly


class NaklonkiListView(generics.ListAPIView):
    queryset = Naklonki.objects.all()
    serializer_class = NaklonkiSerializer
    authentication_classes = (
        rest_framework.authentication.SessionAuthentication,
        rest_framework.authentication.TokenAuthentication,
    )

    def get_queryset(self):
        if "my_deals" in self.request.path:
            user = self.request.user
            queryset = Naklonki.objects.filter(user=user)
            if not queryset.exists():
                return Naklonki.objects.none()
            return queryset
        return Naklonki.objects.all()

    def get(self, request, *args, **kwargs):

        data = self.get_serializer(self.get_queryset(), many=True).data
        if not data:
            return Response(
                {"create": self.request.build_absolute_uri("/api/create/")}, status=200
            )
        total = 0
        is_long = 0
        total_du = 0
        total_fl = 0
        total_vol = 0
        total_ot = 0

        profit_if_1 = {
            "name": "1%",
            "profit": 0,
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }
        profit_if_30 = {
            "name": "30",
            "profit": 0,
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }
        profit_if_50 = {
            "name": "50",
            "profit": 0,
            "DU": 0,
            "FL": 0,
            "VOL": 0,
            "OT": 0,
        }
        profit_if_full = {
            "name": "Full",
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
            profit_if_30["profit"] += i["results"]["profit_if_30"]
            profit_if_50["profit"] += i["results"]["profit_if_50"]
            profit_if_full["profit"] += i["results"]["profit_if_full"]
            if i["form"] == "DU":
                total_du += 1
            elif i["form"] == "FL":
                total_fl += 1
            elif i["form"] == "VOL":
                total_vol += 1
            else:
                total_ot += 1
            if i["results"]["profit_if_full"] > 1:
                profit_if_1[i["form"]] += 1
                profit_if_30[i["form"]] += 1
                profit_if_50[i["form"]] += 1
                profit_if_full[i["form"]] += 1
            elif i["results"]["profit_if_50"] > 1:
                profit_if_1[i["form"]] += 1
                profit_if_30[i["form"]] += 1
                profit_if_50[i["form"]] += 1
            elif i["results"]["profit_if_30"] >= 1:
                profit_if_1[i["form"]] += 1
                profit_if_30[i["form"]] += 1
            elif i["results"]["profit_if_30"] > 0:
                profit_if_30[i["form"]] += 1

            wr_profit_loss = {
                "profit_if_1": {"wins": 0, "losses": 0},
                "profit_if_30": {"wins": 0, "losses": 0},
                "profit_if_50": {"wins": 0, "losses": 0},
                "profit_if_full": {"wins": 0, "losses": 0},
            }

            for i in data:
                if i["results"]["profit_if_1"] > 0:
                    wr_profit_loss["profit_if_1"]["wins"] += 1
                else:
                    wr_profit_loss["profit_if_1"]["losses"] += 1

                if i["results"]["profit_if_30"] > 0:
                    wr_profit_loss["profit_if_30"]["wins"] += 1
                else:
                    wr_profit_loss["profit_if_30"]["losses"] += 1

                if i["results"]["profit_if_50"] > 0:
                    wr_profit_loss["profit_if_50"]["wins"] += 1
                else:
                    wr_profit_loss["profit_if_50"]["losses"] += 1

                if i["results"]["profit_if_full"] > 0:
                    wr_profit_loss["profit_if_full"]["wins"] += 1
                else:
                    wr_profit_loss["profit_if_full"]["losses"] += 1
        profit_if_1["winrate"] = round(
            (wr_profit_loss["profit_if_1"]["wins"] / total * 100) if total > 0 else 0, 2
        )
        profit_if_30["winrate"] = round(
            (wr_profit_loss["profit_if_30"]["wins"] / total * 100) if total > 0 else 0,
            2,
        )
        profit_if_50["winrate"] = round(
            (wr_profit_loss["profit_if_50"]["wins"] / total * 100) if total > 0 else 0,
            2,
        )
        profit_if_full["winrate"] = round(
            (
                (wr_profit_loss["profit_if_full"]["wins"] / total * 100)
                if total > 0
                else 0
            ),
            2,
        )
        summary = {
            "total": total,
            "long": is_long,
            "short": total - is_long,
            "total_du": total_du,
            "total_fl": total_fl,
            "total_vol": total_vol,
            "total_ot": total_ot,
            "profits": {
                "profit_if_1": profit_if_1,
                "profit_if_30": profit_if_30,
                "profit_if_50": profit_if_50,
                "profit_if_full": profit_if_full,
            },
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
    authentication_classes = (
        rest_framework.authentication.SessionAuthentication,
        rest_framework.authentication.TokenAuthentication,
    )
    permission_classes = [IsOwnerOrMentorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NaklonkiCreateView(generics.CreateAPIView):
    queryset = Naklonki.objects.all()
    serializer_class = NaklonkiSerializer
    authentication_classes = (
        rest_framework.authentication.SessionAuthentication,
        rest_framework.authentication.TokenAuthentication,
    )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
