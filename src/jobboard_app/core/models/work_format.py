from django.db import models

from ..models import Base


class WorkFormat(Base):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "work_formats"
