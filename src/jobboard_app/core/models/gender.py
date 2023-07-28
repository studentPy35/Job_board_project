from core.models.base import Base
from django.db import models


class Gender(Base):
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = "genders"
