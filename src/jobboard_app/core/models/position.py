from core.models.base import Base
from django.db import models


class Position(Base):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = "positions"
