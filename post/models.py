from django.db import models

from users.models import User
from utils.models import BaseModel


class Story(BaseModel):
    file = models.FileField(upload_to="stories/")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")

    is_active = models.BooleanField(default=True)
    is_highlight = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user_id} - {self.file.name}"


class UserStoryAction(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_story_actions"
    )
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name="user_story_actions"
    )

    is_liked = models.BooleanField(default=False)
    is_watched = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user_id} - {self.story_id}"


class HashTag(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Post(BaseModel):
    file = models.FileField(upload_to="posts/")
    content = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    tagged = models.ManyToManyField(User, related_name="posts_tagged")
    hash_tags = models.ManyToManyField(HashTag, related_name="posts")

    def __str__(self) -> str:
        return f"{self.user_id}  {self.created_at}"


class UserPostAction(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_post_actions"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="user_post_actions"
    )

    is_liked = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user_id} - {self.post_id}"
