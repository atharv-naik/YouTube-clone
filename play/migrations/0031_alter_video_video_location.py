# Generated by Django 5.0.3 on 2024-05-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("play", "0030_video_stream_url_video_video_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_location",
            field=models.CharField(
                choices=[("local", "Main Server (Local)"), ("s3", "Cloud Server (S3)")],
                default="local",
                max_length=100,
            ),
        ),
    ]
