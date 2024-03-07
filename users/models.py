from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class Gender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    PNS = "PNS", _("Prefer not to say")


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, null=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    image = models.ImageField(upload_to="profile/", blank=True, null=True)

    phone = models.CharField(max_length=13, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    following = models.ManyToManyField(
        "users.User", related_name="followers", blank=True
    )

    website = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=8, choices=Gender.choices, default=Gender.PNS)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
