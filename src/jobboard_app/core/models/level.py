from core.models.base import Base
from django.db import models


class Level(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "levels"
