from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="grades-home"),
    path("faq/", views.faq, name="grades-faq"),
    path("about/", views.about, name="grades-about"),
    path("courses/", views.courses, name="grades-courses"),
    path("course/<int:course_id>/", views.course, name='grades-course'),
    path("course/<int:course_id>/<int:bin_id>", views.assessment, name='grades-assessment'),
    path("courses/new", views.newCourse, name="grades-new-course")
]
