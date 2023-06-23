from django.db import models
from libs.base_models import BaseModel


class Publisher(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
