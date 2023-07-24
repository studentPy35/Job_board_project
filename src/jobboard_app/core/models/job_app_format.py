from django.db import models

from src.jobboard_app.core.models.base import Base


class JobAppFormat(Base):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "app_formats"
