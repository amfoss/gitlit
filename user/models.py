from django.db import models
from django.conf import settings
from django.utils import models
# Create your models here.
class UserQuery(models.Model):
    username = models.ForeginKey(settings.AUTH_USER_MODEL, on_delete=models.cascade)
