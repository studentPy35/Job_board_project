from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.core.files import File


@dataclass
class User:
    name: str
    surname: str
    login: str
    password: str
    email: str
    experience_description: str
    resume: File
    linkedin: str
    github: str
    salary_min: int | None
    salary_max: int | None
    experience: str
    status: str
    level: str
    language: str
    language_level: str
    app_format: str
    work_format: str
    tags: str
