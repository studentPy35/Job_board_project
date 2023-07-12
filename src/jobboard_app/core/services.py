from __future__ import annotations

from typing import TYPE_CHECKING

from core.errors import CompanyAlreadyExistsError, CompanyDoesNotExistError
from core.models import (
    Address,
    Company,
    Country,
    EmployeesQuantityRange,
    JobAppFormat,
    Level,
    Tag,
    Vacancy,
    WorkFormat,
)
from django.db import IntegrityError, transaction
from django.db.models import Count

if TYPE_CHECKING:
    from .dto import CompanyDTO, VacancyDTO


def get_all_vacancies() -> list[Vacancy]:
    vacancies = Vacancy.objects.select_related("level", "company").prefetch_related(
        "tags", "countries", "work_format", "job_app_format"
    )
    return list(vacancies)


def get_all_companies() -> list[Company]:
    companies = (
        Company.objects.select_related("quantity_range", "address")
        .prefetch_related("sector", "review")
        .annotate(vacancy__count=Count("vacancy__id"))
    )
    return list(companies)


def create_vacancy(received_data: VacancyDTO) -> None:
    try:
        with transaction.atomic():
            tags = received_data.tags.split("\r\n")
            tags = [tag.lower() for tag in tags]
            for tag in tags:
                try:
                    Tag.objects.create(name=tag)
                except IntegrityError:
                    continue
            countries = received_data.countries.split("\r\n")
            countries = [country.lower() for country in countries]
            for country in countries:
                try:
                    Country.objects.create(name=country)
                except IntegrityError:
                    continue

            work_formats = received_data.work_format.split("\r\n")
            work_formats = [work_format.lower() for work_format in work_formats]
            for work_format in work_formats:
                try:
                    WorkFormat.objects.create(name=work_format)
                except IntegrityError:
                    continue

            job_app_formats = received_data.job_app_format.split("\r\n")
            job_app_formats = [job_app_format.lower() for job_app_format in job_app_formats]
            for job_app_format in job_app_formats:
                try:
                    JobAppFormat.objects.create(name=job_app_format)
                except IntegrityError:
                    continue

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
            created_vacancy.tags.set(tags)
            created_vacancy.countries.set(countries)
            created_vacancy.work_format.set(work_formats)
            created_vacancy.job_app_format.set(job_app_formats)
    except Company.DoesNotExist:
        raise CompanyDoesNotExistError


def get_position_levels() -> list[tuple[str, str]]:
    levels = [(level.name, level.name) for level in Level.objects.all()]
    return levels


def get_quantity_range() -> list[tuple[str, str]]:
    quantities = [(quantity.name, quantity.name) for quantity in EmployeesQuantityRange.objects.all()]
    return quantities


def create_company(received_data: CompanyDTO) -> None:
    try:
        with transaction.atomic():
            sectors: list[str] = [sector.lower() for sector in received_data.sector.split("\r\n")]
            for sector in sectors:
                try:
                    Tag.objects.create(name=sector)
                except IntegrityError:
                    continue

            quantity_range = EmployeesQuantityRange.objects.get(name=received_data.quantity_range)
            created_address = Address.objects.create(
                city=received_data.city,
                country=received_data.country,
                street=received_data.street,
                house_number=received_data.house_number,
                office_number=received_data.office_number,
            )

            created_company = Company.objects.create(
                name=received_data.name,
                quantity_range=quantity_range,
                foundation_year=received_data.foundation_year,
                logo=received_data.logo,
                description=received_data.description,
                email=received_data.email,
                web_site=received_data.web_site,
                linkedin=received_data.linkedin,
                twitter=received_data.twitter,
                instagram=received_data.instagram,
                address=created_address,
            )

            created_company.sector.set(sectors)

    except IntegrityError:
        raise CompanyAlreadyExistsError
