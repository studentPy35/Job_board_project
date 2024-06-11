from __future__ import annotations

from typing import TYPE_CHECKING

from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import AddCompanyForm, AddReviewForm, AddVacancyForm, ApplyVacancyForm
from .services import (
    Company,
    CompanyStorage,
    Response,
    ResponsesStorage,
    Review,
    ReviewsStorage,
    User,
    VacanciesStorage,
    Vacancy,
)

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


company_storage = CompanyStorage()
vacancy_storage = VacanciesStorage(company=company_storage)
response_storage = ResponsesStorage()
review_storage = ReviewsStorage()


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    vacancy_list = {"vacancy_list": vacancy_storage.get_all_vacancies()}
    return render(request, "core/home.html", vacancy_list)


@require_http_methods(["GET", "POST"])
def add_vacancy(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddVacancyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            position = data.get("position")
            company = data.get("company")
            level = data.get("level")
            experience = data.get("experience")
            salary_min = data.get("salary_min")
            salary_max = data.get("salary_max")
            vacancy = Vacancy(
                position=position,
                company=company,
                level=level,
                experience=experience,
                salary_min=salary_min,
                salary_max=salary_max,
            )
            vacancy_storage.add_vacancy(vacancy)
        return redirect(index)
    else:
        form = AddVacancyForm()
        return render(request, "core/add_vacancy.html", {"title": "Add vacancy", "form": form})


@require_GET
def companies(request: HttpRequest) -> HttpResponse:
    companies_list = {"companies_list": company_storage.get_all_companies()}
    return render(request, "core/companies.html", companies_list)


@require_http_methods(["GET", "POST"])
def add_company(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            company_name = data.get("name")
            employees_number = data.get("employees_number")
            company = Company(name=company_name, employees_number=employees_number)
            company_storage.add_company(company=company)
        return redirect(companies)
    else:
        form = AddCompanyForm()
        return render(request, "core/add_company.html", {"title": "Add company", "form": form})


@require_GET
def get_vacancy(request: HttpRequest, id: int) -> HttpResponse:
    chosen_vacancy = vacancy_storage.get_vacancy_by_id(id=id)
    vacancy = {"vacancy": chosen_vacancy}
    return render(request, "core/vacancy.html", vacancy)


@require_GET
def get_company(request: HttpRequest, id: int) -> HttpResponse:
    chosen_company = company_storage.get_company_by_id(id=id)
    company_review_list = review_storage.get_reviews_by_company_id(id=id)
    company = {"company": chosen_company, "review_list": company_review_list}
    return render(request, "core/company.html", company)


@require_GET
def get_profile_info(request: HttpRequest) -> HttpResponse:
    user_data = User(
        name="Katerina",
        surname="Itchenko",
        login="katerina",
        password="12345",
        email="katerinaitchenko@gmail.com",
        age=34,
        gender="female",
        city="Mozyr",
        country="Belarus",
        experience_description="Learning python",
        linkedin="...",
        github="...",
        experience=0,
        work_format=["full-time", "part-time"],
        position_level="intern",
        job_application_format=["employment contract", "B2B"],
        language_level=[
            {"language": "English", "level": "Upper-Intermidiate"},
            {"language": "Belarusian", "level": "Native"},
        ],
        tags=["python", "developer"],
        id=1,
    )
    context = {"user": user_data}
    return render(request, "core/profile.html", context)


@require_http_methods(["GET", "POST"])
def apply_vacancy(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "POST":
        form = ApplyVacancyForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            description = data.get("description")
            phone = data.get("phone")
            response = Response(resume=data.get("resume"), description=description, phone=phone, vacancy_id=id)
            response_storage.add_response(response)

        return redirect(index)
    else:
        form = ApplyVacancyForm()
        vacancy = vacancy_storage.get_vacancy_by_id(id=id)
        context = {"title": "Apply vacancy", "form": form, "id": id, "vacancy": vacancy}
        return render(request, "core/apply.html", context)


@require_http_methods(["GET", "POST"])
def add_review(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "POST":
        form = AddReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review_text = data.get("review")
            review = Review(review=review_text, company_id=id)
            review_storage.add_review(review=review)
        return redirect(companies)
    else:
        form = AddReviewForm()
        company = company_storage.get_company_by_id(id=id)
        context = {"title": "Apply vacancy", "form": form, "id": id, "company": company}
        return render(request, "core/add_review.html", context)
