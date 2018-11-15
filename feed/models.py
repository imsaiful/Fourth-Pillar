from django.db import models
from django.utils import timezone


# Create your models here.
class Republic(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False, primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField(default="uncategorized")
    Sentiment = models.TextField(default="Positive")


class Indiatoday(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False, primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField(default="uncategorized")
    Sentiment = models.TextField(default="Positive")


class Ndtv(models.Model):
    Headline = models.TextField(null=False)
    Link = models.TextField(null=False, primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField(default="uncategorized")
    Sentiment = models.TextField(default="Positive")
