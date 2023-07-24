from __future__ import annotations

from typing import TYPE_CHECKING

from dacite import from_dict
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from src.jobboard_app.core.business_logic.dto import VacancyDTO
from src.jobboard_app.core.business_logic.errors import CompanyDoesNotExistError
from src.jobboard_app.core.business_logic.services import (
    create_vacancy,
    get_vacancy_by_id,
)
from src.jobboard_app.core.presentation_layer.forms import AddVacancyForm

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


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
        else:
            context = {"title": "Add vacancy", "form": form}
            return render(request, "add_vacancy.html", context)

    else:
        form = AddVacancyForm()
        context = {"title": "Add vacancy", "form": form}
        return render(request, "add_vacancy.html", context)


@require_GET
def get_vacancy(request: HttpRequest, id: int) -> HttpResponse:
    chosen_vacancy, tags, countries, work_formats, job_app_formats = get_vacancy_by_id(id=id)
    context = {
        "vacancy": chosen_vacancy,
        "tags": tags,
        "countries": countries,
        "work_formats": work_formats,
        "job_app_formats": job_app_formats,
    }
    return render(request, "vacancy.html", context)


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
