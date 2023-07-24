from django import forms

from src.jobboard_app.core.business_logic.services import get_quantity_range
from src.jobboard_app.core.presentation_layer.validators import (
    ValidateFileExtension,
    ValidateFileSize,
)


class AddCompanyForm(forms.Form):
    name = forms.CharField(
        label="Company name",
        max_length=100,
        strip=True,
    )
    quantity_range = forms.ChoiceField(choices=get_quantity_range(), label="Employees number", required=False)
    foundation_year = forms.IntegerField(label="Foundation year", required=False, min_value=1800)
    logo = forms.ImageField(
        label="Company's logo",
        allow_empty_file=False,
        validators=[ValidateFileSize(max_size=5000000), ValidateFileExtension(["png"])],
        required=False,
    )
    description = forms.CharField(
        label="Description", widget=forms.Textarea, max_length=800, strip=True, required=False
    )
    email = forms.EmailField(label="Email", required=False)
    phone = forms.CharField(label="Phone number", required=False, strip=True, max_length=25)
    web_site = forms.URLField(label="Web site", required=False)
    linkedin = forms.URLField(label="LinkedIn", required=False)
    twitter = forms.URLField(label="Twitter", required=False)
    instagram = forms.URLField(label="Instagram", required=False)
    city = forms.CharField(label="City", required=False, max_length=50, strip=True)
    country = forms.CharField(label="Country", required=False, max_length=50, strip=True)
    street = forms.CharField(label="Street", required=False, max_length=50, strip=True)
    house_number = forms.IntegerField(label="House number", required=False, min_value=1)
    office_number = forms.IntegerField(label="House number", required=False, min_value=1)
    sectors = forms.CharField(label="Sectors", required=False, max_length=50, strip=True)
