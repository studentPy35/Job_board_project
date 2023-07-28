from core.models.base import Base
from django.db import models


class Language(Base):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "languages"
