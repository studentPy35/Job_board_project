from dataclasses import dataclass


@dataclass
class AddressDTO:
    city: str
    country: str
    street: str
    house_number: int
    office_number: int
