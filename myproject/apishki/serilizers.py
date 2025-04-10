from rest_framework import serializers
from .models import Naklonki


class NaklonkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naklonki
        fields = [
            "pk",
            "token_name",
            "deal_result",
            "deal_potential",
            "form",
            "comment",
            "img_url",
            "user",
        ]
