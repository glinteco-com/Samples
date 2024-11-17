from typing import Iterable
from django.db import models
from polls.tasks import calculate_birth_year

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    year = models.IntegerField(blank=True, null=True)
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.year = calculate_birth_year(self.age)
        return super().save(force_insert=True)
    