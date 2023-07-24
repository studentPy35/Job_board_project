# from __future__ import annotations
#
# from typing import TYPE_CHECKING
#
# from core.business_logic.dto import CompanyDTO, VacancyDTO
# from core.business_logic.errors import CompanyDoesNotExistError
# from core.business_logic.services import (
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
#     return render(request, "profile.html", context)
#
