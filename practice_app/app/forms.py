from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from unidecode import unidecode

from . import models


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class FirmForm(forms.ModelForm):
    class Meta:
        model = models.Firm
        fields = [
            "title",
            "slug",
            "main_inf",
            "photo",
            "location",
            "place",
            "productions",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.HiddenInput(attrs={"class": "form-control"}),
            "main_inf": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "productions": forms.SelectMultiple(attrs={"class": "form-control"}),
            "place": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def clean_slug(self):
        self.cleaned_data["slug"] = slugify(unidecode(self.cleaned_data["title"]))
        return self.cleaned_data["slug"]


class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = ["place"]
        widgets = {
            "place": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProductionForm(forms.ModelForm):
    class Meta:
        model = models.Production
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
        }


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = [
            "name",
            "slug",
            "main_inf",
            "photo",
            "age",
            "gender",
            "adress",
            "nationality",
            "family_status",
            "profession",
            "education",
            "experience",
            "current_place",
            "telegram",
            "viber",
            "skype",
            "mail",
            "phone",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.HiddenInput(attrs={"class": "form-control"}),
            "main_inf": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "age": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.TextInput(attrs={"class": "form-control"}),
            "adress": forms.TextInput(attrs={"class": "form-control"}),
            "nationality": forms.TextInput(attrs={"class": "form-control"}),
            "family_status": forms.TextInput(attrs={"class": "form-control"}),
            "profession": forms.TextInput(attrs={"class": "form-control"}),
            "education": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "current_place": forms.Select(attrs={"class": "form-control"}),
            "telegram": forms.TextInput(attrs={"class": "form-control"}),
            "viber": forms.TextInput(attrs={"class": "form-control"}),
            "skype": forms.TextInput(attrs={"class": "form-control"}),
            "mail": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_slug(self):
        self.cleaned_data["slug"] = slugify(unidecode(self.cleaned_data["name"]))
        return self.cleaned_data["slug"]
