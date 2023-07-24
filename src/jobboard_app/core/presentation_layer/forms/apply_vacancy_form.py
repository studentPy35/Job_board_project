from django import forms


class ApplyVacancyForm(forms.Form):
    description = forms.CharField(label="Description", max_length=500, strip=True)
    resume = forms.FileField(label="Resume")
    phone = forms.CharField(label="Phone number", max_length=100)
