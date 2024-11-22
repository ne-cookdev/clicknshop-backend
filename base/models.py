from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator

User = get_user_model()
