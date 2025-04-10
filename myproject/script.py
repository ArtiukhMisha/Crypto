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
    naklonki.deal_potential = random.choice(["STOP", "33", "50", "100", "MORE"])
    naklonki.save()
