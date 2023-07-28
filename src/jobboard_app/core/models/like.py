from core.models.base import Base
from django.db import models


class Like(Base):
    name = models.BooleanField()
    review = models.ForeignKey(to="Review", on_delete=models.CASCADE, related_name="likes", related_query_name="like")
    user = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name="likes", related_query_name="like")

    class Meta:
        db_table = "likes"
        unique_together = (("user", "review"),)
