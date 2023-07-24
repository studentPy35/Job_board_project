from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.core.files import File


@dataclass
class CompanyDTO:
    name: str
    quantity_range: str
    foundation_year: int
    logo: File
    description: str
    email: str
    phone: str | None
    web_site: str
    linkedin: str | None
    twitter: str | None
    instagram: str | None
    city: str
    country: str
    street: str | None
    house_number: int | None
    office_number: int | None
    sectors: str
