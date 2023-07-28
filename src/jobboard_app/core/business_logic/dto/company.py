from __future__ import annotations

from dataclasses import dataclass

from django.core.files.uploadedfile import InMemoryUploadedFile


@dataclass
class CompanyDTO:
    name: str
    quantity_range: str
    foundation_year: int | None
    logo: InMemoryUploadedFile | None
    description: str | None
    email: str | None
    phone: str | None
    web_site: str | None
    linkedin: str | None
    twitter: str | None
    instagram: str | None
    city: str | None
    country: str | None
    street: str | None
    house_number: int | None
    office_number: int | None
    sectors: str | None
