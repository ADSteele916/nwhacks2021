from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        views.ExtraLoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        views.ExtraLogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
]
