# Generated by Django 5.0.3 on 2024-06-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utm_tracker", "0010_sitehit_http_referer_traffic_http_referer"),
    ]

    operations = [
        migrations.AddField(
            model_name="traffic",
            name="ip_address",
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
