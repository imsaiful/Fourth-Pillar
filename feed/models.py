from django.db import models
from django.utils import timezone


# Create your models here.
class Republic(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField(null=True)
    Sentiment = models.TextField(null=True)

    def __str__(self):
        return self.Headline

    class Meta:
        ordering = ["-Date"]


class Indiatoday(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField(null=True)
    Sentiment = models.TextField(null=True)

    def __str__(self):
        return self.Headline

    class Meta:
        ordering = ["-Date"]


class Ndtv(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField(null=True)
    Sentiment = models.TextField(null=True)

    def __str__(self):
        return self.Headline

    class Meta:
        ordering = ["-Date"]
