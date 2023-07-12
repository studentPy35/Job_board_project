from __future__ import annotations

from typing import TYPE_CHECKING

from core.errors import CompanyDoesNotExistError
from core.forms import AddCompanyForm, AddVacancyForm
from core.services import (
    create_company,
    create_vacancy,
    get_all_companies,
    get_all_vacancies,
)
from dacite import from_dict
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods
from dto import CompanyDTO, VacancyDTO

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    vacancies = get_all_vacancies()
    context = {"vacancy_list": vacancies}
    return render(request, "core/home.html", context)


@require_http_methods(["GET", "POST"])
def add_vacancy(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddVacancyForm(request.POST)
        if form.is_valid():
            data = from_dict(VacancyDTO, form.cleaned_data)
            try:
                create_vacancy(received_data=data)
            except CompanyDoesNotExistError:
                return HttpResponseBadRequest(content="Provided company doesn't exist.")
        return redirect(index)
    else:
        form = AddVacancyForm()
        return render(request, "core/add_vacancy.html", {"title": "Add vacancy", "form": form})


@require_GET
def companies(request: HttpRequest) -> HttpResponse:
    context = {"companies_list": get_all_companies()}
    return render(request, "core/companies.html", context)


@require_http_methods(["GET", "POST"])
def add_company(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            received_data = from_dict(CompanyDTO, form.cleaned_data)
            try:
                create_company(received_data=received_data)
            except CompanyDoesNotExistError:
                return HttpResponseBadRequest(content="Such company already exists.")
        return redirect(companies)
    else:
        form = AddCompanyForm()
        return render(request, "core/add_company.html", {"title": "Add company", "form": form})


#
# @require_GET
# def get_vacancy(request: HttpRequest, id: int) -> HttpResponse:
#     chosen_vacancy = vacancy_storage.get_vacancy_by_id(id=id)
#     vacancy = {"vacancy": chosen_vacancy}
#     return render(request, "core/vacancy.html", vacancy)
#
#
# @require_GET
# def get_company(request: HttpRequest, id: int) -> HttpResponse:
#     chosen_company = company_storage.get_company_by_id(id=id)
#     company_review_list = review_storage.get_reviews_by_company_id(id=id)
#     company = {"company": chosen_company, "review_list": company_review_list}
#     return render(request, "core/company.html", company)
#
#
# @require_GET
# def get_profile_info(request: HttpRequest) -> HttpResponse:
#     user_data = User(
#         name="Katerina",
#         surname="Itchenko",
#         login="katerina",
#         password="12345",
#         email="katerinaitchenko@gmail.com",
#         age=34,
#         gender="female",
#         city="Mozyr",
#         country="Belarus",
#         experience_description="Learning python",
#         linkedin="...",
#         github="...",
#         experience=0,
#         work_format=["full-time", "part-time"],
#         position_level="intern",
#         job_application_format=["employment contract", "B2B"],
#         language_level=[
#             {"language": "English", "level": "Upper-Intermidiate"},
#             {"language": "Belarusian", "level": "Native"},
#         ],
#         tags=["python", "developer"],
#         id=1,
#     )
#     context = {"user": user_data}
#     return render(request, "core/profile.html", context)
#
#
# @require_http_methods(["GET", "POST"])
# def apply_vacancy(request: HttpRequest, id: int) -> HttpResponse:
#     if request.method == "POST":
#         form = ApplyVacancyForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             description = data.get("description")
#             phone = data.get("phone")
#             response = Response(resume=data.get("resume"), description=description, phone=phone, vacancy_id=id)
#             response_storage.add_response(response)
#
#         return redirect(index)
#     else:
#         form = ApplyVacancyForm()
#         vacancy = vacancy_storage.get_vacancy_by_id(id=id)
#         context = {"title": "Apply vacancy", "form": form, "id": id, "vacancy": vacancy}
#         return render(request, "core/apply.html", context)
#
#
# @require_http_methods(["GET", "POST"])
# def add_review(request: HttpRequest, id: int) -> HttpResponse:
#     if request.method == "POST":
#         form = AddReviewForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             review_text = data.get("review")
#             review = Review(review=review_text, company_id=id)
#             review_storage.add_review(review=review)
#         return redirect(companies)
#     else:
#         form = AddReviewForm()
#         company = company_storage.get_company_by_id(id=id)
#         context = {"title": "Apply vacancy", "form": form, "id": id, "company": company}
#         return render(request, "core/add_review.html", context)
