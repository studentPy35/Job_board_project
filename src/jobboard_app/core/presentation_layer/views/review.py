# from __future__ import annotations
#
# from typing import TYPE_CHECKING
#
# from core.business_logicdto import CompanyDTO, VacancyDTO
# from core.business_logicerrors import CompanyDoesNotExistError
# from core.business_logicservices import (
#     create_company,
#     create_vacancy,
#     get_all_companies,
#     get_all_vacancies,
#     get_company_by_id,
#     get_vacancy_by_id,
#     search_vacancies,
# )
# from core.presentation_layer.forms import (
#     AddCompanyForm,
#     AddVacancyForm,
#     FilterVacancyForm,
# )
# from dacite import from_dict
# from django.http import HttpResponseBadRequest
# from django.shortcuts import redirect, render
# from django.views.decorators.http import require_GET, require_http_methods
#
# if TYPE_CHECKING:
#     from django.http import HttpRequest, HttpResponse
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
#         return render(request, "add_review.html", context)
