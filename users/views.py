from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.shortcuts import redirect, render

from users.forms import UserRegisterForm


class ExtraLoginView(LoginView):
    def get_context_data(self, **kwargs):
        view_context = super().get_context_data(**kwargs)
        view_context.update({"title": "Log In"})
        return view_context


class ExtraLogoutView(LogoutView):
    def get_context_data(self, **kwargs):
        view_context = super().get_context_data(**kwargs)
        view_context.update({"title": "Log Out"})
        return view_context


class ExtraPasswordResetView(PasswordResetView):
    def get_context_data(self, **kwargs):
        view_context = super().get_context_data(**kwargs)
        view_context.update({"title": "Reset Password"})
        return view_context


class ExtraPasswordResetDoneView(PasswordResetDoneView):
    def get_context_data(self, **kwargs):
        view_context = super().get_context_data(**kwargs)
        view_context.update({"title": "Reset Password"})
        return view_context


class ExtraPasswordResetConfirmView(PasswordResetConfirmView):
    def get_context_data(self, **kwargs):
        view_context = super().get_context_data(**kwargs)
        view_context.update({"title": "Confirm Password Reset"})
        return view_context


class ExtraPasswordResetCompleteView(PasswordResetCompleteView):
    def get_context_data(self, **kwargs):
        view_context = super().get_context_data(**kwargs)
        view_context.update({"title": "Password Reset!"})
        return view_context


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")

            new_user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, new_user)

            message = "Your account is now good to go!"
            messages.success(request, message)

            return redirect("grades-home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
