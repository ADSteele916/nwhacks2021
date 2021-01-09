from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("A user with that username already exists.")

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("A user with that email address already exists.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]