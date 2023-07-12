from django.db import models

from ..models import Base


class LanguageLevel(Base):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "language_levels"
