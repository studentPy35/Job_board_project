from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from django.db import IntegrityError, transaction
from django.db.models import Count

from src.jobboard_app.core.business_logic.errors import CompanyAlreadyExistsError
from src.jobboard_app.core.models import (
    Address,
    Company,
    EmployeesQuantityRange,
    Sector,
)

if TYPE_CHECKING:
    from src.jobboard_app.core.business_logic.dto import CompanyDTO


def get_all_companies() -> list[Company]:
    companies = (
        Company.objects.select_related("quantity_range", "address")
        .prefetch_related("sector", "review")
        .annotate(vacancy__count=Count("vacancy__id"))
    )
    return list(companies)


def get_company_by_id(id: int) -> tuple[Company, list[str]]:
    company = (
        Company.objects.select_related("quantity_range", "address").prefetch_related("sector", "review").get(pk=id)
    )
    sectors = company.sector.all()
    return company, list(sectors)


def create_company(received_data: CompanyDTO) -> None:
    try:
        with transaction.atomic():
            sectors: list[str] = [sector.lower() for sector in received_data.sectors.split("\r\n")]
            related_sectors = []
            for sector in sectors:
                try:
                    received_sector = Sector.objects.get_or_create(name=sector)[0]
                except IntegrityError:
                    continue
                related_sectors.append(received_sector)

            quantity_range = EmployeesQuantityRange.objects.get(name=received_data.quantity_range)
            created_address = Address.objects.create(
                city=received_data.city,
                country=received_data.country,
                street=received_data.street,
                house_number=received_data.house_number,
                office_number=received_data.office_number,
            )
            file_extension = received_data.logo.name.split(".")[-1]
            file_name = str(uuid.uuid4())
            received_data.logo.name = file_name + "." + file_extension

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

            created_company.sector.set(related_sectors)

    except IntegrityError:
        raise CompanyAlreadyExistsError
