from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .managers import NewsletterManager, RssFeedManager

User = get_user_model()


class Newsletter(models.Model):
    uuid = models.UUIDField()
    audio_url = models.URLField(blank=True, null=True, max_length=2000)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    objects = NewsletterManager()

    class Meta:
        unique_together = ["content_type", "object_id"]

    def __str__(self):
        return f"{self.content_type} - {self.object_id}"


class Dictionary(models.Model):
    word = models.CharField(max_length=254, unique=True)
    pronunciation = models.CharField(max_length=254)

    class Meta:
        ordering = ["word"]
        verbose_name_plural = "Dictionaries"

    def __str__(self):
        return f"{self.word} - [{self.pronunciation}]"


class RssFeed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    feed = models.URLField(blank=True, null=True)

    objects = RssFeedManager()

    def __str__(self):
        return f"{self.user} - {self.feed}"
