from django.contrib.auth.models import AbstractUser
from django.db import models
from users.utils.functions import upload_path_avatar_handler


class User(AbstractUser):
    avatar = models.ImageField(upload_to=upload_path_avatar_handler)
