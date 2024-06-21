# Generated by Django 5.0.3 on 2024-06-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utm_tracker", "0009_sitehit_user_agent_traffic_user_agent"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitehit",
            name="http_referer",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="traffic",
            name="http_referer",
            field=models.URLField(blank=True, null=True),
        ),
    ]
