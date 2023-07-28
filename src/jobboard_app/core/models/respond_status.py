from core.models.base import Base
from django.db import models


class RespondStatus(Base):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "respond_statuses"
