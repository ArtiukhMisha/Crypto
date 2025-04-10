from rest_framework import serializers
from .models import Naklonki
from decimal import Decimal


class ResultSerializer(serializers.Serializer):
    profit_if_1 = serializers.SerializerMethodField()
    profit_if_30 = serializers.SerializerMethodField()
    profit_if_50 = serializers.SerializerMethodField()
    profit_if_full = serializers.SerializerMethodField()

    def get_profit_if_30(self, obj):
        if obj.deal_potential in ["33", "50", "100", "MORE"]:
            return obj.profit_if_full * Decimal(0.33)
        return -1

    def get_profit_if_50(self, obj):
        if obj.deal_potential in ["50", "100", "MORE"]:
            return obj.profit_if_full * Decimal(0.5)
        return -1

    def get_profit_if_full(self, obj):
        if obj.deal_potential in ["100", "MORE"]:
            return obj.profit_if_full
        return -1

    def get_profit_if_1(self, obj):
        if (
            obj.deal_potential in ["33", "50", "100", "MORE"]
            and self.get_profit_if_30(obj) > 1
        ):
            return 1
        elif (
            obj.deal_potential in ["50", "100", "MORE"]
            and self.get_profit_if_50(obj) > 1
        ):
            return 1
        return -1


class NaklonkiSerializer(serializers.ModelSerializer):

    results = ResultSerializer(source="*", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Naklonki
        fields = [
            "pk",
            "date",
            "token_name",
            "is_long",
            "form",
            "comment",
            "img_url",
            "username",
            "results",
        ]
