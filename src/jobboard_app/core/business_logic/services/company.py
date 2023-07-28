from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from core.business_logic.errors import CompanyAlreadyExistsError
from core.business_logic.services.common import (
    change_file_size,
    replace_file_name_to_uuid,
)
from core.models import Address, Company, EmployeesQuantityRange, Sector
from django.db import IntegrityError, transaction
from django.db.models import Count

if TYPE_CHECKING:
    from core.business_logic.dto import CompanyDTO


logger = logging.getLogger(__name__)


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
    logger.info("Got company.", extra={"company_id": id, "company": company.name})
    return company, list(sectors)


def create_company(received_data: CompanyDTO) -> None:
    try:
        with transaction.atomic():
            if received_data.sectors:
                sectors: list[str] = [sector.lower() for sector in received_data.sectors.split("\r\n")]
                related_sectors = []
                for sector in sectors:
                    received_sector, created = Sector.objects.get_or_create(name=sector)
                    if created:
                        related_sectors.append(received_sector)

            quantity_range = EmployeesQuantityRange.objects.get(name=received_data.quantity_range)
            created_address = Address.objects.create(
                city=received_data.city,
                country=received_data.country,
                street=received_data.street,
                house_number=received_data.house_number,
                office_number=received_data.office_number,
            )
            if received_data.logo:
                received_data.logo = replace_file_name_to_uuid(file=received_data.logo)
                received_data.logo = change_file_size(file=received_data.logo)

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
            logger.info("Company has been created.", extra={"company_name": received_data.name})

    except IntegrityError:
        logger.error("Such company already exists.", extra={"company_name": received_data.name})
        raise CompanyAlreadyExistsError
