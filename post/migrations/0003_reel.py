# Generated by Django 4.2.7 on 2024-03-07 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post", "0002_alter_story_users_liked_alter_story_users_watched"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "hash_tags",
                    models.ManyToManyField(related_name="reels", to="post.hashtag"),
                ),
                (
                    "tagged",
                    models.ManyToManyField(
                        related_name="reels_tagged", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reels",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "users_liked",
                    models.ManyToManyField(
                        related_name="reels_liked", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "users_saved",
                    models.ManyToManyField(
                        related_name="reels_saved", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
