from django.conf import settings as django_settings
from django.db import models
from yarr.models import Feed


class UserFeeds(models.Model):
    user = models.ForeignKey(django_settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feeds = models.ManyToManyField(Feed)
