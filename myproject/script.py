import os
import django
import random

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Initialize Django
django.setup()

from apishki.models import Naklonki
from django.db import connection

for naklonki in Naklonki.objects.all():
    naklonki.profit_if_full = random.uniform(0, 1000)
    naklonki.save()
