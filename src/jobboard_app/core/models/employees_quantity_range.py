from django.db import models

from src.jobboard_app.core.models.base import Base


class EmployeesQuantityRange(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "employees_quantity_ranges"
