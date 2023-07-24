from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.core.files import File


@dataclass
class Respond:
    user: str
    vacancy: str
    description: str
    resume: File
    phone: str
    respond_status: str
