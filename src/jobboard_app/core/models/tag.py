from django.db import models

from ..models import Base


class Tag(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "tags"
