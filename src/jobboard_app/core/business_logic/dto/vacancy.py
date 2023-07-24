from dataclasses import dataclass


@dataclass
class VacancyDTO:
    name: str
    experience: str
    description: str | None
    min_salary: int | None
    max_salary: int | None
    level: str
    company: str
    tags: str
    countries: str
    work_format: str
    job_app_format: str
