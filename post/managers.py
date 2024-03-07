from django.db import models
from django.utils import timezone


class StoryManager(models.Manager):

    def all_active(self):
        return self.filter(
            created_at__gte=timezone.now() - timezone.timedelta(hours=24)
        )
