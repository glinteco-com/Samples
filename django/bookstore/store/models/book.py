from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from libs.base_models import BaseModel


class Book(BaseModel):
    publisher = models.ForeignKey(
        "Publisher", on_delete=models.CASCADE, related_name="books"
    )
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="books"
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="books"
    )

    title = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @cached_property
    def is_expensive(self):
        return self.price >= Decimal("100")  # $100

    @cached_property
    def is_old(self):
        return self.published_date < timezone.localtime() - timezone.timedelta(
            days=365
        )
