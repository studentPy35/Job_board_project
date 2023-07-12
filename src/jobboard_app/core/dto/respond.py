from dataclasses import dataclass


@dataclass
class Respond:
    user: str
    vacancy: str
    description: str
    resume: str
    phone: str
    respond_status: str
