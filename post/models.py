from django.db import models

from users.models import User
from post.managers import StoryManager
from utils.models import BaseModel


class Story(BaseModel):
    file = models.FileField(upload_to="stories/")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")

    is_active = models.BooleanField(default=True)
    is_highlight = models.BooleanField(default=False)

    users_watched = models.ManyToManyField(
        User, related_name="stories_watched", blank=True
    )
    users_liked = models.ManyToManyField(User, related_name="stories_liked", blank=True)

    objects = StoryManager()

    def __str__(self) -> str:
        return f"{self.user_id} - {self.file.url}"


class HashTag(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Post(BaseModel):
    content = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    tagged = models.ManyToManyField(User, related_name="posts_tagged")
    hash_tags = models.ManyToManyField(HashTag, related_name="posts")

    users_liked = models.ManyToManyField(User, related_name="posts_liked")
    users_saved = models.ManyToManyField(User, related_name="posts_saved")
    users_viewed = models.ManyToManyField(User, related_name="post_viewed")

    def __str__(self) -> str:
        return f"{self.user_id}  {self.created_at}"


class File(BaseModel):
    file = models.FileField(upload_to="posts/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="files")

    def __str__(self) -> str:
        return self.file.url


class Reel(BaseModel):
    video = models.FileField(upload_to="reels/")

    content = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reels")

    tagged = models.ManyToManyField(User, related_name="reels_tagged", blank=True)
    hash_tags = models.ManyToManyField(HashTag, related_name="reels", blank=True)

    users_liked = models.ManyToManyField(User, related_name="reels_liked", blank=True)
    users_saved = models.ManyToManyField(User, related_name="reels_saved", blank=True)

    def __str__(self) -> str:
        return f"{self.user_id}  {self.created_at}"
