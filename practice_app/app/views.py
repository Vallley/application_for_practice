from django.contrib import messages
from django.contrib.auth import login, logout
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

from . import forms, models


def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("firms_page")
        else:
            messages.error(request, "Ошибка регистрации")

    else:
        form = forms.UserRegisterForm()
    return render(request, "app/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = forms.UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("firms_page")
    else:
        form = forms.UserLoginForm()
    return render(request, "app/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


class MenuInf:
    def get_place(self):
        return models.Place.objects.all()

    def get_production(self):
        return models.Production.objects.all()


class FirmView(MenuInf, ListView):
    model = models.Firm
    template_name = "app/firms_page.html"
    context_object_name = "firms"
    paginate_by = 10

    def get_max_count(self):
        print("5")
        return 5


class FilterFirmsView(MenuInf, ListView):
    template_name = "app/firms_page.html"
    context_object_name = "firms"

    def get_queryset(self):
        queryset = models.Firm.objects.filter(
            Q(place__in=self.request.GET.getlist("place"))
            | Q(productions__in=self.request.GET.getlist("production"))
        )
        return queryset.distinct()


class CreateFirm(CreateView):
    form_class = forms.FirmForm
    template_name = "app/add_firm.html"


class CreatePlace(CreateView):
    form_class = forms.PlaceForm
    template_name = "app/add_place.html"
    success_url = "/"


class CreateProduction(CreateView):
    form_class = forms.ProductionForm
    template_name = "app/add_production.html"
    success_url = "/"


class CreatePerson(CreateView):
    form_class = forms.PersonForm
    template_name = "app/add_person.html"


class PersonView(ListView):
    model = models.Person
    template_name = "app/people_page.html"
    context_object_name = "people"
    paginate_by = 20


class FirmPage(DetailView):
    template_name = "app/firm.html"
    context_object_name = "firm"

    def get_queryset(self):
        return models.Firm.objects.filter(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["firm"] = self.get_object()
        firm = models.Firm.objects.annotate(Count("person"))
        for i in firm:
            if i == self.object:
                self.object.count_person = i.person__count
                self.object.save()
                self.object.refresh_from_db()
        return context


class PersonPage(DetailView):
    template_name = "app/person.html"
    context_object_name = "person"

    def get_queryset(self):
        return models.Person.objects.filter(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person"] = self.get_object()
        return context
