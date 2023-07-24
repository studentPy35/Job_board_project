from django import forms

from src.jobboard_app.core.business_logic.services import get_position_levels


class FilterVacancyForm(forms.Form):
    name = forms.CharField(label="Vacancy name", max_length=100, strip=True, required=False)
    experience = forms.CharField(label="Experience", max_length=100, strip=True, required=False)
    min_salary = forms.IntegerField(min_value=1, label="Minimal salary", required=False)
    max_salary = forms.IntegerField(min_value=1, label="Maximal salary", required=False)
    company = forms.CharField(label="Company name", max_length=100, strip=True, required=False)
    level = forms.ChoiceField(choices=[("", "All")] + get_position_levels(), label="Level", required=False)
    tags = forms.CharField(label="Tag", required=False)
    countries = forms.CharField(label="Country", required=False)
    work_format = forms.CharField(label="Work format", max_length=30, strip=True, required=False)
    job_app_format = forms.CharField(label="Job application format", max_length=30, strip=True, required=False)
