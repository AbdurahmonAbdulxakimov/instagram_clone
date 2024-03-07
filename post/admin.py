from django.contrib import admin

from post import models


@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "user_id", "is_active", "is_highlight"]
    list_filter = ["user_id", "is_active", "is_highlight"]


@admin.register(models.Reel)
class ReelAdmin(admin.ModelAdmin):
    list_display = ["id", "video", "user_id"]
