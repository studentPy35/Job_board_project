from __future__ import annotations
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from dataclasses import dataclass
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.http import HttpResponse, HttpRequest


@dataclass
class Vacancy:
    position: str
    company: str
    level: str
    experience: int
    salary: int


@dataclass
class Company:
    name: str
    vacancies: int


class VacanciesStorage:
    vacancy_list: list[Vacancy] = []
    companies: list[Company] = []

    def add(self,  vacancy: Vacancy) -> None:
        self.vacancy_list.append(vacancy)
        flag = True
        for company in self.companies:
            if company.name == vacancy.company:
                company.vacancies += 1
                flag = False
        if flag:
            self.companies.append(Company(name=vacancy.company, vacancies=1))


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    vacancy_list = {
        'vacancy_list': VacanciesStorage.vacancy_list
    }
    return render(request, 'core/home.html', vacancy_list)


@require_http_methods(['GET', 'POST'])
def add(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        position = request.POST.get('position', None)
        company = request.POST.get('company', None)
        level = request.POST.get('level', None)
        experience = request.POST.get('experience', None)
        salary = request.POST.get('salary', None)
        vacancy = Vacancy(
            position=position,
            company=company,
            level=level,
            experience=experience,
            salary=salary
        )
        VacanciesStorage().add(vacancy)
        return render(request, 'core/add.html', {'title': 'Add vacancy'})
    else:
        return render(request, 'core/add.html', {'title': 'Add vacancy'})


@require_GET
def companies(request: HttpRequest) -> HttpResponse:
    companies_list = {
        'companies_list': VacanciesStorage.companies
    }
    return render(request, 'core/companies.html', companies_list)
