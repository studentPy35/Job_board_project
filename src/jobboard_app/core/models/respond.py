from django.db import models

from ..models import Base


class Respond(Base):
    user = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name="responds", related_query_name="respond")
    vacancy = models.ForeignKey(
        to="Vacancy", on_delete=models.CASCADE, related_name="responds", related_query_name="respond"
    )
    description = models.TextField(max_length=500, null=True)
    resume = models.FileField(upload_to="users_resume", unique=True)
    phone = models.CharField(max_length=25, null=True)
    respond_status = models.ForeignKey(
        to="RespondStatus", on_delete=models.SET_NULL, null=True, related_name="responds", related_query_name="respond"
    )

    class Meta:
        db_table = "responds"
