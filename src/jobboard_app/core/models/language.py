from django.db import models

from ..models import Base


class Language(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "languages"
