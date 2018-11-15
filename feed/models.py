from django.db import models
from django.utils import timezone


# Create your models here.
class Republic(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False, primary_key=True)
    Date = models.DateTimeField(default=timezone.now, null=True)
    Category = models.TextField(default="uncategorized", null=True)
    Sentiment = models.TextField(default="Positive", null=True)

    def __str__(self):
        return self.Headline

    class Meta:
        ordering = ["-Date"]


class Indiatoday(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False, primary_key=True)
    Date = models.DateTimeField(default=timezone.now, null=True)
    Category = models.TextField(default="uncategorized", null=True)
    Sentiment = models.TextField(default="Positive", null=True)

    def __str__(self):
        return self.Headline

    class Meta:
        ordering = ["-Date"]


class Ndtv(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False, primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField(default="uncategorized")
    Sentiment = models.TextField(default="Positive")

    def __str__(self):
        return self.Headline

    class Meta:
        ordering = ["-Date"]
