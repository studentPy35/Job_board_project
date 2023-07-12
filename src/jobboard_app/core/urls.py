from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vacancy/add/", views.add_vacancy, name="add_vacancy"),
    path("company/", views.companies, name="companies"),
    path("company/add/", views.add_company, name="add_company"),
    # path("vacancy/<int:id>/", views.get_vacancy, name="vacancy"),
    # path("company/<int:id>/", views.get_company, name="company"),
    # path("profile/", views.get_profile_info, name="profile"),
    # path("vacancy/<int:id>/apply/", views.apply_vacancy, name="apply"),
    # path("company/<int:id>/review/", views.add_review, name="review"),
]
