from rest_framework import serializers
from .models import Naklonki
from decimal import Decimal
from rest_framework.reverse import reverse


class ResultSerializer(serializers.Serializer):
    profit_if_1 = serializers.SerializerMethodField()
    profit_if_30 = serializers.SerializerMethodField()
    profit_if_50 = serializers.SerializerMethodField()
    profit_if_full = serializers.SerializerMethodField()

    def get_profit_if_30(self, obj):
        if obj.deal_potential in ["30", "50", "100", "MORE"]:
            return obj.profit_if_full * Decimal(0.30)
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
            obj.deal_potential in ["30", "50", "100", "MORE"]
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
    username = serializers.ReadOnlyField(source="user.username")
    deal_potential = serializers.ChoiceField(
        choices=[
            ("30", "30%"),
            ("50", "50%"),
            ("100", "100%"),
            ("STOP", "STOP"),
            ("MORE", "Больше"),
        ],
        write_only=True,
    )
    profit_if_full = serializers.DecimalField(
        max_digits=10, decimal_places=2, write_only=True
    )
    details_url = serializers.SerializerMethodField()
    form_display = serializers.CharField(source="get_form_display", read_only=True)

    class Meta:
        model = Naklonki
        fields = [
            "pk",
            "date",
            "token_name",
            "is_long",
            "deal_potential",
            "profit_if_full",
            "form",
            "form_display",
            "comment",
            "img_url",
            "username",
            "results",
            "details_url",
        ]

    def get_details_url(self, obj, format=None):
        request = self.context.get("request")
        return reverse(
            "naklonki-crud",
            args=[obj.pk],
            request=request,
            format=format,
        )
