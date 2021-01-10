from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="grades-home"),
    path("faq/", views.faq, name="grades-faq"),
    path("about/", views.about, name="grades-about"),
    path("<int:user_id>/courses/", views.courses, name="grades-courses"),
    path("<int:user_id>/course/<int:course_id>/", views.course, name='grades-course'),
    path("<int:user_id>/course/<int:course_id>/<int:bin_id>", views.assessment, name='grades-assessment'),
    path("<int:user_id>/courses/new", views.newCourse, name="grades-new-course")
]
