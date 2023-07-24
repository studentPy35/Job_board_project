from django.db import models

from src.jobboard_app.core.models.base import Base


class Gender(Base):
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = "genders"
