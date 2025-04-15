from datetime import date
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Naklonki(models.Model):
    class Meta:
        ordering = ["-id"]

    DUGA = "DU"
    FLAT = "FL"
    VOL = "VOL"
    OTHER = "OT"
    MOVEMENT_TYPE_CHOICES = [
        (DUGA, "Дуга"),
        (FLAT, "Плоская"),
        (VOL, "Волатильность"),
        (OTHER, "Неопределенная"),
    ]
    THIRTY = "33"
    HALF = "50"
    FULL = "100"
    STOP = "STOP"
    MORE = "MORE"
    RESULT_TYPE_CHOICES = [
        (THIRTY, "33%"),
        (HALF, "50%"),
        (FULL, "100%"),
        (STOP, "STOP"),
        (MORE, "Больше"),
    ]
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    token_name = models.CharField(max_length=15, blank=False)
    is_long = models.BooleanField(default=True)
    deal_potential = models.CharField(
        max_length=5,
        blank=False,
        choices=RESULT_TYPE_CHOICES,
    )
    profit_if_full = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    form = models.CharField(max_length=8, default=OTHER, choices=MOVEMENT_TYPE_CHOICES)
    comment = models.TextField(max_length=500, blank=True)
    img_url = models.URLField(max_length=500, blank=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.token_name

    @property
    def missed_profit(self):
        return f"{self.deal_potential} - {self.deal_result} "
