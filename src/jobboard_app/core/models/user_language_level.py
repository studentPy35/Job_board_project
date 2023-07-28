from core.models.base import Base
from django.db import models


class UserLanguageLevel(Base):
    user = models.ForeignKey(to="User", on_delete=models.CASCADE)
    language = models.ForeignKey(to="Language", on_delete=models.CASCADE)
    language_level = models.ForeignKey(to="LanguageLevel", on_delete=models.CASCADE)

    class Meta:
        db_table = "users_languages_levels"
