from core.models.base import Base
from django.db import models


class Status(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "statuses"
