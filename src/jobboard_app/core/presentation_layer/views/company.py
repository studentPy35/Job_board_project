from __future__ import annotations

from typing import TYPE_CHECKING

from dacite import from_dict
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from src.jobboard_app.core.business_logic.dto import CompanyDTO
from src.jobboard_app.core.business_logic.errors import CompanyDoesNotExistError
from src.jobboard_app.core.business_logic.services import (
    create_company,
    get_all_companies,
    get_company_by_id,
)
from src.jobboard_app.core.presentation_layer.forms import AddCompanyForm

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@require_GET
def companies(request: HttpRequest) -> HttpResponse:
    context = {"companies_list": get_all_companies()}
    return render(request, "companies.html", context)


@require_http_methods(["GET", "POST"])
def add_company(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            received_data = from_dict(CompanyDTO, form.cleaned_data)
            try:
                create_company(received_data=received_data)
                return redirect(companies)
            except CompanyDoesNotExistError:
                return HttpResponseBadRequest(content="Such company already exists.")
        else:
            context = {"title": "Add company", "form": form}
            return render(request, "add_company.html", context)
    else:
        form = AddCompanyForm()
        context = {"title": "Add company", "form": form}
        return render(request, "add_company.html", context)


@require_GET
def get_company(request: HttpRequest, id: int) -> HttpResponse:
    chosen_company, sectors = get_company_by_id(id=id)
    # company_review_list = review_storage.get_reviews_by_company_id(id=id)
    # "review_list": company_review_list
    context = {"company": chosen_company, "sectors": sectors}
    return render(request, "company.html", context)
