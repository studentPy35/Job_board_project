from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import IntegrityError, transaction

from src.jobboard_app.core.business_logic.errors import CompanyDoesNotExistError
from src.jobboard_app.core.models import (
    Company,
    Country,
    JobAppFormat,
    Level,
    Tag,
    Vacancy,
    WorkFormat,
)

if TYPE_CHECKING:
    from src.jobboard_app.core.business_logic.dto import VacancyDTO


def get_all_vacancies() -> list[Vacancy]:
    vacancies = Vacancy.objects.select_related("level", "company").prefetch_related(
        "tags", "countries", "work_format", "job_app_format"
    )

    return list(vacancies)


def get_vacancy_by_id(id: int) -> tuple[Vacancy, list[str], list[str], list[str], list[str]]:
    vacancy = (
        Vacancy.objects.select_related("level", "company")
        .prefetch_related("tags", "countries", "work_format", "job_app_format")
        .get(pk=id)
    )
    tags = list(vacancy.tags.all())
    countries = list(vacancy.countries.all())
    work_formats = list(vacancy.work_format.all())
    print([item.name for item in work_formats])
    job_app_formats = list(vacancy.job_app_format.all())
    return vacancy, tags, countries, work_formats, job_app_formats


def create_vacancy(received_data: VacancyDTO) -> None:
    try:
        with transaction.atomic():
            tags = [tag.lower() for tag in received_data.tags.split("\r\n")]
            related_tags = []
            for tag in tags:
                try:
                    received_tag = Tag.objects.get_or_create(name=tag)[0]
                except IntegrityError:
                    continue
                related_tags.append(received_tag)

            countries = [country.lower() for country in received_data.countries.split("\r\n")]
            related_countries = []
            for country in countries:
                try:
                    received_country = Country.objects.get_or_create(name=country)[0]
                except IntegrityError:
                    continue
                related_countries.append(received_country)

            work_formats = [work_format.lower() for work_format in received_data.work_format.split("\r\n")]
            related_work_formats = []
            for work_format in work_formats:
                try:
                    received_work_format = WorkFormat.objects.get_or_create(name=work_format)[0]
                except IntegrityError:
                    continue
                related_work_formats.append(received_work_format)

            job_app_formats = received_data.job_app_format.split("\r\n")
            job_app_formats = [job_app_format.lower() for job_app_format in job_app_formats]
            related_job_app_format = []
            for job_app_format in job_app_formats:
                try:
                    received_job_app_format = JobAppFormat.objects.get_or_create(name=job_app_format)[0]
                except IntegrityError:
                    continue
                related_job_app_format.append(received_job_app_format)

            level = Level.objects.get(name=received_data.level)
            company = Company.objects.get(name=received_data.company)

            created_vacancy = Vacancy.objects.create(
                name=received_data.name,
                level=level,
                company=company,
                expirience=received_data.experience,
                min_salary=received_data.min_salary,
                max_salary=received_data.max_salary,
                description=received_data.description,
            )
            created_vacancy.tags.set(related_tags)
            created_vacancy.countries.set(related_countries)
            created_vacancy.work_format.set(related_work_formats)
            created_vacancy.job_app_format.set(related_job_app_format)
    except Company.DoesNotExist:
        raise CompanyDoesNotExistError


def search_vacancies(received_data: VacancyDTO) -> list[Vacancy]:
    vacancies = Vacancy.objects.select_related("level", "company").prefetch_related(
        "tags", "countries", "work_format", "job_app_format"
    )
    if received_data.name:
        vacancies = vacancies.filter(name__icontains=received_data.name)
    if received_data.experience:
        vacancies = vacancies.filter(expirience__icontains=received_data.experience)
    if received_data.min_salary:
        vacancies = vacancies.filter(min_salary__gte=received_data.min_salary)
    if received_data.max_salary:
        vacancies = vacancies.filter(max_salary__lte=received_data.max_salary)
    if received_data.company:
        vacancies = vacancies.filter(company__name__icontains=received_data.company)
    if received_data.level:
        vacancies = vacancies.filter(level__name=received_data.level)
    if received_data.tags:
        vacancies = vacancies.filter(tags__name__icontains=received_data.tags)
    if received_data.countries:
        vacancies = vacancies.filter(countries__name__icontains=received_data.countries)
    if received_data.work_format:
        vacancies = vacancies.filter(work_format__name__icontains=received_data.work_format)
    if received_data.job_app_format:
        vacancies = vacancies.filter(job_app_format__name__icontains=received_data.job_app_format)

    return list(vacancies)
