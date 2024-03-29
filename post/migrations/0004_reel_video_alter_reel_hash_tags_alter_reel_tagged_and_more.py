# Generated by Django 4.2.7 on 2024-03-07 13:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post", "0003_reel"),
    ]

    operations = [
        migrations.AddField(
            model_name="reel",
            name="video",
            field=models.FileField(default=1, upload_to="reels/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="reel",
            name="hash_tags",
            field=models.ManyToManyField(
                blank=True, related_name="reels", to="post.hashtag"
            ),
        ),
        migrations.AlterField(
            model_name="reel",
            name="tagged",
            field=models.ManyToManyField(
                blank=True, related_name="reels_tagged", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="reel",
            name="users_liked",
            field=models.ManyToManyField(
                blank=True, related_name="reels_liked", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="reel",
            name="users_saved",
            field=models.ManyToManyField(
                blank=True, related_name="reels_saved", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
