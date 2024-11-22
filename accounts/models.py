from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager


class User(AbstractUser):
    """
    Модель сущности пользователя.
    """
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(default=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    role = models.CharField(max_length=35, default="user")
    difficulty_level = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(255), ],
        default=100,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
