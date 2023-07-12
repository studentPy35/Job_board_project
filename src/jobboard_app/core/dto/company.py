from dataclasses import dataclass


@dataclass
class CompanyDTO:
    name: str
    quantity_range: str
    foundation_year: int
    logo: str
    description: str
    email: str
    phone: str
    web_site: str
    linkedin: str
    twitter: str
    instagram: str
    city: str
    country: str
    street: str
    house_number: int
    office_number: int
    sector: str
