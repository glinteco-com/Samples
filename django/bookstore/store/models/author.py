from django.db import models
from django_countries.fields import CountryField
from libs.base_models import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    country = CountryField()
