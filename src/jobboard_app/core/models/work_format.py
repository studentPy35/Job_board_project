from core.models.base import Base
from django.db import models


class WorkFormat(Base):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "work_formats"
