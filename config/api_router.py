from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import UserViewSet
from post import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = [
    path("profile/<int:pk>/", views.ProfileRetrieveAPIView.as_view(), name="profile"),
    #
    path("stories/", views.StoryListAPIView.as_view(), name="stories"),
    path("stories/<int:pk>/", views.StoryRetrieveAPIView.as_view(), name="story"),
    #
    path("reels/", views.ReelListAPIView.as_view(), name="reels"),
    path("reels/<int:pk>/", views.ReelRetrieveAPIView.as_view(), name="reel"),
]
urlpatterns += router.urls
