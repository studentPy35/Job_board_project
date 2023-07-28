from django import forms


class AddReviewForm(forms.Form):
    review = forms.CharField(label="Review", max_length=800, strip=True)
