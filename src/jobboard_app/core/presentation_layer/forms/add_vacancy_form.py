from core.business_logic.services import get_position_levels
from core.presentation_layer.validators import TagsValidator
from django import forms


class AddVacancyForm(forms.Form):
    name = forms.CharField(label="Vacancy name", max_length=100, strip=True)
    experience = forms.CharField(label="Experience", max_length=100, strip=True)
    description = forms.CharField(
        label="Description", widget=forms.Textarea, max_length=800, strip=True, required=False
    )
    min_salary = forms.IntegerField(min_value=1, label="Minimal salary", required=False)
    max_salary = forms.IntegerField(min_value=1, label="Maximal salary", required=False)
    company = forms.CharField(label="Company name", max_length=100, strip=True)
    level = forms.ChoiceField(choices=get_position_levels(), label="Level")
    tags = forms.CharField(label="Tags", widget=forms.Textarea, validators=[TagsValidator(max_number=5)])
    country = forms.CharField(label="Countries", widget=forms.Textarea, max_length=100)
    work_format = forms.CharField(label="Work format", max_length=30, strip=True)
    job_app_format = forms.CharField(label="Job application format", max_length=30, strip=True)
