from django.db import models

from users.models import User
from post.models import Story, Post, Reel
from utils.models import BaseModel


class Message(BaseModel):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_sent"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_recieved"
    )

    content = models.TextField()
    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies")
    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name="user_message",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.content[:16]


class UserReaction(BaseModel):
    content = models.CharField(max_length=64)
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="reactions"
    )

    def __str__(self) -> str:
        return self.content


# class UserMessage(BaseModel):
#     from_user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="messages_sent"
#     )
#     to_user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="messages_received"
#     )
#     message = models.ForeignKey(
#         Message, on_delete=models.CASCADE, related_name="user_message"
#     )

#     def __str__(self) -> str:
#         return f"{self.from_user_id} to {self.to_user_id}"


class Chat(BaseModel):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="chats")

    def __str__(self) -> str:
        return self.title


class UserGroupMessage(BaseModel):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_group_sent"
    )
    to_group = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="messages_group_received"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="user_group_message"
    )

    def __str__(self) -> str:
        return f"{self.from_user_id} to {self.to_group_id}"


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", blank=True, null=True
    )
    reel = models.ForeignKey(
        Reel, on_delete=models.CASCADE, related_name="comments", blank=True, null=True
    )

    content = models.TextField()

    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies")
    users_liked = models.ManyToManyField(User, related_name="comments_liked")

    def __str__(self) -> str:
        return f"{self.user_id} to {self.post_id}"
