from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Vacancy:
    position: str
    company: str
    level: str
    experience: int
    salary_min: int | None
    salary_max: int | None
    id: int = 0


@dataclass
class Company:
    name: str
    employees_number: int
    id: int = 0
    vacancies: int = 0


@dataclass
class User:
    name: str
    login: str
    password: str
    email: str
    age: int
    gender: str
    city: str
    country: str
    experience_description: str
    linkedin: str
    github: str
    experience: int
    work_format: list[str]
    position_level: str
    job_application_format: list[str]
    language_level: list[dict[str, str]]
    tags: list[str]
    status: str = "open to work"
    photo: str | None = None
    resume: str | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    phone: str | None = None
    surname: str | None = None
    id: int | None = None


@dataclass
class Response:
    description: str
    resume: object
    phone: str
    status: str = "created"
    vacancy_id: int | None = None
    user_id: int = 1
    id: int | None = None


@dataclass
class Review:
    review: str
    user_id: int | None = None
    id: int | None = None
    company_id: int | None = None


class CompanyAlreadyExistsError(Exception):
    ...


class CompanyNotExistsError(Exception):
    ...


class CompanyStorage:
    ID_COUNTER = 0

    def __init__(self) -> None:
        self._companies: list[Company] = []

    def _validate_company(self, company: Company) -> None:
        for item in self._companies:
            if item.name.lower() == company.name.lower():
                raise CompanyAlreadyExistsError

    def add_company(self, company: Company) -> None:
        self._validate_company(company=company)
        self.ID_COUNTER += 1
        company.id = self.ID_COUNTER
        self._companies.append(company)

    def get_all_companies(self) -> list[Company]:
        return self._companies

    def get_company_by_id(self, id: int) -> Company | None:
        company_list = self.get_all_companies()
        last = len(company_list) - 1
        first = 0
        while last >= first:
            middle = round((last + first) / 2)
            if company_list[middle].id == id:
                return company_list[middle]
            elif company_list[middle].id > id:
                last = middle - 1
            else:
                first = middle + 1
        return None


class VacanciesStorage:
    ID_COUNTER = 0

    def __init__(self, company: CompanyStorage) -> None:
        self._company = company
        self._vacancy_list: list[Vacancy] = []

    def add_vacancy(self, vacancy: Vacancy) -> None:
        flag = False
        for company in self._company.get_all_companies():
            if vacancy.company.lower() == company.name.lower():
                flag = True
                company.vacancies += 1
        if flag:
            self.ID_COUNTER += 1
            vacancy.id = self.ID_COUNTER
            self._vacancy_list.append(vacancy)
        else:
            raise CompanyNotExistsError

    def get_all_vacancies(self) -> list[Vacancy]:
        return self._vacancy_list

    def get_vacancy_by_id(self, id: int) -> Vacancy | None:
        vacancy_list = self.get_all_vacancies()
        last = len(vacancy_list) - 1
        first = 0
        while last >= first:
            middle = round((last + first) / 2)
            if vacancy_list[middle].id == id:
                return vacancy_list[middle]
            elif vacancy_list[middle].id > id:
                last = middle - 1
            else:
                first = middle + 1
        return None


class ResponsesStorage:
    ID_COUNTER = 0

    def __init__(self) -> None:
        self._responses_list: list[Response] = []

    def add_response(self, response: Response) -> None:
        self.ID_COUNTER += 1
        response.id = self.ID_COUNTER
        self._responses_list.append(response)


class ReviewsStorage:
    ID_COUNTER = 0

    def __init__(self) -> None:
        self._reviews_list: list[Review] = []

    def add_review(self, review: Review) -> None:
        self.ID_COUNTER += 1
        review.id = self.ID_COUNTER
        self._reviews_list.append(review)

    def get_reviews_by_company_id(self, id: int) -> list[Review] | None:
        reviews = []
        for review in self._reviews_list:
            if review.company_id == id:
                reviews.append(review)
        if reviews:
            return reviews
        else:
            return None
