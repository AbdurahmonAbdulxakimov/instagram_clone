from rest_framework import serializers

from post import models
from users.models import User
from messanger.models import Comment


class SimpleUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "image")


class StorySerializer(serializers.ModelSerializer):
    user = SimpleUser()
    users_watched = SimpleUser(many=True, read_only=True)
    users_liked = SimpleUser(many=True, read_only=True)

    class Meta:
        model = models.Story
        fields = (
            "id",
            "file",
            "user",
            "is_active",
            "is_highlight",
            "users_watched",
            "users_liked",
            "created_at",
        )


class UserSerializer(serializers.ModelSerializer):
    following = SimpleUser(many=True)
    followers = SimpleUser(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "bio",
            "phone",
            "gender",
            "website",
            "following",
            "followers",
        )


class SimpleCommentSerializer(serializers.ModelSerializer):
    user = SimpleUser()

    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "user",
        )


class CommentSerializer(serializers.ModelSerializer):
    user = SimpleUser()
    reply = SimpleCommentSerializer()
    users_liked = SimpleUser(many=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "reply",
            "content",
            "user",
            "reel",
            "post",
            "users_liked",
        )


class ReelSerializer(serializers.ModelSerializer):
    user = SimpleUser()
    users_liked = SimpleUser(many=True)
    users_saved = SimpleUser(many=True)
    tagged = SimpleUser(many=True)

    class Meta:
        model = models.Reel
        fields = (
            "id",
            "video",
            "content",
            "user",
            "tagged",
            "hash_tags",
            "users_liked",
            "users_saved",
            "comments",
            "created_at",
        )
