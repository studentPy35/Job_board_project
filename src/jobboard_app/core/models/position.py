from django.db import models

from ..models import Base


class Position(Base):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = "positions"
