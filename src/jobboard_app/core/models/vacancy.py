from django.db import models

from src.jobboard_app.core.models.base import Base


class Vacancy(Base):
    name = models.CharField(max_length=100)
    expirience = models.CharField(max_length=30)
    description = models.TextField(null=True)
    min_salary = models.PositiveIntegerField(null=True)
    max_salary = models.PositiveIntegerField(null=True)
    level = models.ForeignKey(to="Level", on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, related_name="vacancies", related_query_name="vacancy"
    )
    employee = models.ForeignKey(
        to="Employee", on_delete=models.SET_NULL, null=True, related_name="vacancies", related_query_name="vacancy"
    )
    tags = models.ManyToManyField(to="Tag", related_name="vacancies", db_table="vacancies_tags")
    countries = models.ManyToManyField(to="Country", related_name="vacancies", db_table="vacancies_country")
    work_format = models.ManyToManyField(to="WorkFormat", related_name="vacancies", db_table="vacancies_work_formats")
    job_app_format = models.ManyToManyField(
        to="JobAppFormat", related_name="vacancies", db_table="vacancies_app_formats"
    )

    class Meta:
        db_table = "vacancies"
