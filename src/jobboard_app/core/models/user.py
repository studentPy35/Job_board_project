from django.db import models

from ..models import Base


class User(Base):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    experience_description = models.TextField(max_length=1000)
    resume = models.FileField(upload_to="users_resume", unique=True)
    linkedin = models.URLField(unique=True)
    github = models.URLField(unique=True)
    min_salary = models.PositiveIntegerField(null=True)
    max_salary = models.PositiveIntegerField(null=True)
    experience = models.CharField(max_length=20)
    profile = models.OneToOneField(to="Profile", on_delete=models.CASCADE)
    status = models.ForeignKey(
        to="Status", on_delete=models.SET_NULL, null=True, related_name="users", related_query_name="user"
    )
    level = models.ForeignKey(
        to="Level", on_delete=models.SET_NULL, null=True, related_name="users", related_query_name="users"
    )
    language = models.ManyToManyField(to="Language", related_name="users", through="UserLanguageLevel")
    app_format = models.ManyToManyField(to="JobAppFormat", related_name="users", db_table="users_job_app_format")
    work_format = models.ManyToManyField(to="WorkFormat", related_name="users", db_table="users_work_format")
    tags = models.ManyToManyField(to="Tag", related_name="users", db_table="users_tags")

    class Meta:
        db_table = "users"
