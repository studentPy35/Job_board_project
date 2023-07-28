from core.models.base import Base
from django.db import models


class Company(Base):
    name = models.CharField(max_length=200, unique=True)
    quantity_range = models.ForeignKey(
        to="EmployeesQuantityRange",
        on_delete=models.SET_NULL,
        null=True,
        related_name="companies",
        related_query_name="company",
    )
    foundation_year = models.PositiveIntegerField(null=True)
    logo = models.ImageField(upload_to="companies_logo")
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=25)
    web_site = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    twitter = models.URLField(null=True)
    instagram = models.URLField(null=True)
    address = models.OneToOneField(
        to="Address", on_delete=models.SET_NULL, null=True, related_name="companies", related_query_name="company"
    )
    sector = models.ManyToManyField(to="Sector", related_name="companies", db_table="companies_sectors")
    review = models.ManyToManyField(to="Review", related_name="companies", db_table="companies_reviews")

    class Meta:
        db_table = "companies"
