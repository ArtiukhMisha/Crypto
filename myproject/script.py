import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Initialize Django
django.setup()

from apishki.models import Naklonki
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM naklonki_naklonki")
    rows = cursor.fetchall()

for row in rows:
    (
        _id,  # skip the ID from source
        token_name,
        deal_result,
        deal_potential,
        form,
        comment,
        img_url,
        _user_id,  # assuming you don’t need this
        _active,   # assuming this isn't used in apishki
    ) = row

    Naklonki.objects.create(
        token_name=token_name,
        deal_result=deal_result,
        deal_potential=deal_potential,
        form=form,
        comment=comment,
        img_url=img_url
    )