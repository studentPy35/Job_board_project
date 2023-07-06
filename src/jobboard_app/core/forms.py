from django import forms


class AddCompanyForm(forms.Form):
    name = forms.CharField(
        label="Company name",
        max_length=100,
        strip=True,
    )
    employees_number = forms.IntegerField(min_value=1, label="Employees number")


class AddVacancyForm(forms.Form):
    position = forms.CharField(label="Vacancy name", max_length=100, strip=True)
    company = forms.CharField(label="Company name", max_length=100, strip=True)
    level = forms.ChoiceField(
        choices=(("Intern", "Intern"), ("Junior", "Junior"), ("Middle", "Middle"), ("Senior", "Senior")), label="Level"
    )
    experience = forms.CharField(label="Experience", max_length=100, strip=True)
    salary_min = forms.IntegerField(min_value=1, label="Minimal salary", required=False)
    salary_max = forms.IntegerField(min_value=1, label="Maximal salary", required=False)


class ApplyVacancyForm(forms.Form):
    description = forms.CharField(label="Description", max_length=500, strip=True)
    resume = forms.FileField(label="Resume")
    phone = forms.CharField(label="Phone number", max_length=100)


class AddReviewForm(forms.Form):
    review = forms.CharField(label="Review", max_length=800, strip=True)
