from django.db import models

from ..models import Base


class Profile(Base):
    phone = models.CharField(max_length=30, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.ForeignKey(
        to="Gender", on_delete=models.SET_NULL, null=True, related_name="profiles", related_query_name="profile"
    )
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=30, null=True)
    photo = models.ImageField(upload_to="users_photo")

    class Meta:
        db_table = "profiles"
