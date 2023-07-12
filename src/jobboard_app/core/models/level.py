from django.db import models

from ..models import Base


class Level(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "levels"
