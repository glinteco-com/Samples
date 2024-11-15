from django.contrib.sites.models import Site
from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=200)
    sites = models.ManyToManyField(Site)
    