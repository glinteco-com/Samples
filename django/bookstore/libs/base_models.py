from django.core import serializers
from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}"

    def to_json(self):
        return serializers.serialize("json", [self])

    def to_dict(self):
        return model_to_dict(self)
