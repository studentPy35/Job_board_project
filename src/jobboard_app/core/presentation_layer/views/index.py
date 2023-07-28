from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from core.business_logic.dto import VacancyDTO
from core.business_logic.services import search_vacancies
from core.presentation_layer.converters import convert_data_from_form_to_dto
from core.presentation_layer.forms import FilterVacancyForm
from django.shortcuts import render
from django.views.decorators.http import require_GET

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

logger = logging.getLogger(__name__)


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    form = FilterVacancyForm(request.GET)
    if form.is_valid():
        received_data = form.cleaned_data
        data = convert_data_from_form_to_dto(VacancyDTO, received_data)
        vacancies = search_vacancies(received_data=data)
        form = FilterVacancyForm()
        context = {"vacancy_list": vacancies, "form": form}
        return render(request, "home.html", context)
    else:
        context = {"form": form}
        return render(request, "home.html", context)
