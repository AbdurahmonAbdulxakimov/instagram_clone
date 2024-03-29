# Generated by Django 4.2.7 on 2024-03-07 11:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="users_liked",
            field=models.ManyToManyField(
                blank=True, related_name="stories_liked", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="story",
            name="users_watched",
            field=models.ManyToManyField(
                blank=True, related_name="stories_watched", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
