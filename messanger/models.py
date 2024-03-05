from django.db import models

from users.models import User
from utils.models import BaseModel


class Message(BaseModel):
    content = models.TextField()
    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies")

    def __str__(self) -> str:
        return self.content[:16]


class UserReaction(BaseModel):
    content = models.CharField(max_length=64)
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="reactions"
    )

    def __str__(self) -> str:
        return self.content


class UserMessage(BaseModel):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_sent"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_received"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="user_message"
    )
    # story = models.ForeignKey(
    #     Story, on_delete=models.CASCADE, related_name="user_message"
    # )

    def __str__(self) -> str:
        return f"{self.from_user__username} to {self.to_user__username}"


class Group(BaseModel):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="groups")

    def __str__(self) -> str:
        return self.title


class UserGroupMessage(BaseModel):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_group_sent"
    )
    to_group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="messages_group_received"
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="user_group_message"
    )

    def __str__(self) -> str:
        return f"{self.from_user__username} to {self.to_group__title}"
