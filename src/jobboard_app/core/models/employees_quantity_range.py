from django.db import models

from ..models import Base


class EmployeesQuantityRange(Base):
    name = models.CharField(unique=True)

    class Meta:
        db_table = "employees_quantity_ranges"
