from __future__ import annotations

from typing import TYPE_CHECKING

from dacite import from_dict
from django.shortcuts import render
from django.views.decorators.http import require_GET

from src.jobboard_app.core.business_logic.dto import VacancyDTO
from src.jobboard_app.core.business_logic.services import (
    get_all_vacancies,
    search_vacancies,
)
from src.jobboard_app.core.presentation_layer.forms import FilterVacancyForm

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    form = FilterVacancyForm(request.GET)
    if form.is_valid():
        received_data = form.cleaned_data
        data = from_dict(VacancyDTO, received_data)
        vacancies = search_vacancies(received_data=data)
        form = FilterVacancyForm()
        context = {"vacancy_list": vacancies, "form": form}
        return render(request, "home.html", context)
    else:
        form = FilterVacancyForm()
        vacancies = get_all_vacancies()
        context = {"vacancy_list": vacancies, "form": form}
        return render(request, "home.html", context)
