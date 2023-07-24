from django.db import models

from src.jobboard_app.core.models.base import Base


class RespondStatus(Base):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "respond_statuses"
