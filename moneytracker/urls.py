"""Module for moneytracker urls in the Django application."""

from django.urls import path

from .views import (
    TrackerView, AboutView, ContactView,
    check_email
)

app_name = "moneytracker"

urlpatterns = [
    path("", TrackerView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),

    path("api/check-email/", check_email, name="check_email")
]
