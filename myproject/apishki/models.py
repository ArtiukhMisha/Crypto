from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Naklonki(models.Model):
    DUGA = "DU"
    FLAT = "FL"
    VOL = "VOL"
    OTHER = "OT"
    MOVEMENT_TYPE_CHOICES = [
        (DUGA, "Дуга"),
        (FLAT, "Плоская"),
        (VOL, "Высокая волатильность"),
        (OTHER, "Неопределенная"),
    ]
    ONE = "1"
    THIRTY = "33"
    HALF = "50"
    FULL = "100"
    STOP = "STOP"
    MORE = "MORE"
    RESULT_TYPE_CHOICES = [
        (ONE, "1%"),
        (THIRTY, "33%"),
        (HALF, "50%"),
        (FULL, "100%"),
        (STOP, "STOP"),
        (MORE, "Больше"),
    ]
    id = models.AutoField(primary_key=True)
    token_name = models.CharField(max_length=15, blank=False)  # Removed required=True
    deal_result = models.CharField(
        max_length=5,
        blank=False,
        choices=RESULT_TYPE_CHOICES,  # Removed required=True
    )
    deal_potential = models.CharField(
        max_length=5,
        blank=False,
        choices=RESULT_TYPE_CHOICES,  # Removed required=True
    )
    form = models.CharField(max_length=8, default=OTHER, choices=MOVEMENT_TYPE_CHOICES)
    comment = models.TextField(max_length=500, blank=True)
    img_url = models.URLField(max_length=500, blank=True)
    user = models.ForeignKey(
        User, default=1, null=True, on_delete=models.SET_NULL
    )  # Removed required=True

    def __str__(self):
        return self.token_name

    @property
    def missed_profit(self):
        return f"{self.deal_potential} - {self.deal_result} "

    