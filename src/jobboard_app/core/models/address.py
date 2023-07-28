from core.models.base import Base
from django.db import models


class Address(Base):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=50, null=True)
    house_number = models.PositiveIntegerField(null=True)
    office_number = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = "addresses"
