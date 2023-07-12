from django.db import models

from ..models import Base


class Employee(Base):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, related_name="employees", related_query_name="employee"
    )
    phone = models.CharField(max_length=25)
    password = models.CharField(max_length=25, unique=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="employees_photo")
    position = models.ManyToManyField(to="Position", related_name="employees", db_table="employees_positions")

    class Meta:
        db_table = "employees"
