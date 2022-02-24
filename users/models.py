from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGING_KAKAO = "kakao"

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGING_KAKAO, "Kakao"),
    )


    email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    superhost = models.BooleanField(default=False)
    favs = models.ManyToManyField("rooms.Room", related_name="favs")

    # description = models.CharField(max_length=180)
    # gender = models.CharField(
    #     _("gender"), choices=GENDER_CHOICES, max_length=10, blank=True
    # )
    # birthdate = models.DateField(blank=True, null=True)
    # login_method = models.CharField(
    #     max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    # )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def room_count(self):
        return self.rooms.count()

    room_count.short_description = "Room Count"
