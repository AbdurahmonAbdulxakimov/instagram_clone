from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q, F
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from post import serializers, models
from users.models import User


class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class StoryListAPIView(ListAPIView):
    queryset = models.Story.objects.all_active()
    serializer_class = serializers.StorySerializer

    def get_queryset(self) -> QuerySet:
        return (
            (
                super()
                .get_queryset()
                .filter(
                    Q(user__in=self.request.user.following.all())
                    | Q(user_id=self.request.user.id)
                )
            )
            .select_related("user")
            .prefetch_related("users_watched", "users_liked", "user__following")
        )


class StoryRetrieveAPIView(RetrieveAPIView):
    queryset = models.Story.objects.all_active()
    serializer_class = serializers.StorySerializer

    def get(self, request, *args: Any, **kwargs: Any) -> Response:
        self.get_object().users_watched.add(self.request.user)
        return super().get(request, *args, **kwargs)


class ReelListAPIView(ListAPIView):
    queryset = (
        models.Reel.objects.all()
        .select_related("user")
        .prefetch_related(
            "tagged",
            "users_liked",
            "users_saved",
            "hash_tags",
            "comments",
            "comments__user",
            "comments__reply",
            "comments__users_liked",
        )
    )
    serializer_class = serializers.ReelSerializer


class ReelRetrieveAPIView(RetrieveAPIView):
    queryset = (
        models.Reel.objects.all()
        .select_related("user")
        .prefetch_related(
            "tagged",
            "users_liked",
            "users_saved",
            "hash_tags",
            "comments",
            "comments__user",
            "comments__reply",
            "comments__users_liked",
        )
    )
    serializer_class = serializers.ReelSerializer


class ExpoloreAPIView(generics.ListAPIView):
    def get_queryset(self, request):
        # QUERY
        my_friends_liked = User.objects.filter(
            models.Q(following=requst.user)|
            models.Q(followers=request.user)).filter(
            models.Q(posts_saved__id=models.OuterRef("id")) |
            models.Q(posts_liked__id = models.OuterRef("id"))
            ).count()
        posts = Post.objects.annotate(
            user_liked_count=models.Count("users_liked",filter=models.Q(users_liked___created_at__gte=timezone.now()-timezone.timedelte(hour=36))),
            liked_friends_count = models.Subquery(my_friends_liked)
            comments_count = models.Count("comments")
            ).filter(
            models.Q(user_liked_count__gte = 10_000) | 
            models.Q(liked_friends_count__gte=5)
            models.Q(comments_count__gte=10_000)
        ).exclude(users_viewed=request.user).order_by("?")[:100]

        post_ids = posts.values("id")
        Post.objects.filter(id__in=post_ids).update(users_views=request.id) 

        return posts