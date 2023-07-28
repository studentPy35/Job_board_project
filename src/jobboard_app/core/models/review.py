from core.models.base import Base
from django.db import models


class Review(Base):
    review = models.TextField(max_length=800)
    author = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name="reviews", related_query_name="review")

    class Meta:
        db_table = "reviews"
