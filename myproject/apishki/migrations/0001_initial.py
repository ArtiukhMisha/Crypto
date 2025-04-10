# Generated by Django 5.2 on 2025-04-10 08:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Naklonki',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token_name', models.CharField(max_length=15)),
                ('deal_result', models.CharField(choices=[('1', '1%'), ('33', '33%'), ('50', '50%'), ('100', '100%'), ('STOP', 'STOP'), ('MORE', 'Больше')], max_length=5)),
                ('deal_potential', models.CharField(choices=[('1', '1%'), ('33', '33%'), ('50', '50%'), ('100', '100%'), ('STOP', 'STOP'), ('MORE', 'Больше')], max_length=5)),
                ('form', models.CharField(choices=[('DU', 'Дуга'), ('FL', 'Плоская'), ('VOL', 'Высокая волатильность'), ('OT', 'Неопределенная')], default='OT', max_length=8)),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('img_url', models.URLField(blank=True, max_length=500)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
