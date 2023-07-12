from django.db import models

from ..models import Base


class Address(Base):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.PositiveIntegerField()
    office_number = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = "addresses"
