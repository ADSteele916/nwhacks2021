from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="grades-home"),
    path("faq/", views.faq, name="grades-faq"),
    path("about/", views.about, name="grades-about"),
    path("courses/", views.courses, name="grades-courses")
]
