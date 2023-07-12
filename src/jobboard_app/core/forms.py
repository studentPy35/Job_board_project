from django import forms

from .services import get_position_levels, get_quantity_range


class AddCompanyForm(forms.Form):
    name = forms.CharField(
        label="Company name",
        max_length=100,
        strip=True,
    )
    quantity_range = forms.ChoiceField(choices=get_quantity_range(), label="Employees number", required=False)
    foundation_year = forms.IntegerField(label="Foundation year", required=False, min_value=1800)
    logo = forms.ImageField(label="Company's logo", required=False)
    description = forms.Textarea()
    email = forms.EmailField(label="Email", required=False, strip=True)
    phone = forms.CharField(label="Phone number", required=False, strip=True, max_length=25)
    web_site = forms.URLField(label="Web site", required=False)
    linkedin = forms.URLField(label="LinkedIn", required=False)
    twitter = forms.URLField(label="Twitter", required=False)
    instagram = forms.URLField(label="Instagram", required=False)
    city = forms.CharField(label="City", required=False, max_length=50, strip=True)
    country = forms.CharField(label="Country", required=False, max_length=50, strip=True)
    street = forms.CharField(label="Street", required=False, max_length=50, strip=True)
    house_number = forms.IntegerField(label="House number", required=False, min_value=1, strip=True)
    office_number = forms.IntegerField(label="House number", required=False, min_value=1, strip=True)
    sectors = forms.CharField(label="Sectors", required=False, max_length=50, strip=True)


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
    tags = forms.CharField(label="Tags", widget=forms.Textarea)
    countries = forms.CharField(label="Countries", widget=forms.Textarea)
    work_format = forms.CharField(label="Work format", max_length=30, strip=True)
    job_app_format = forms.CharField(label="Job application format", max_length=30, strip=True)


class ApplyVacancyForm(forms.Form):
    description = forms.CharField(label="Description", max_length=500, strip=True)
    resume = forms.FileField(label="Resume")
    phone = forms.CharField(label="Phone number", max_length=100)


class AddReviewForm(forms.Form):
    review = forms.CharField(label="Review", max_length=800, strip=True)
