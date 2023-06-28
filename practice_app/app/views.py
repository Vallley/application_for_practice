from typing import Any, Dict
from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.db.models import Q
from django.db.models import Count
from .forms import FirmForm


class MenuInf:
    def get_place(self):
        return Place.objects.all()
    
    def get_production(self):
        return Production.objects.all()

class FirmView(MenuInf, ListView):
    model = Firm
    template_name = 'app/firms_page.html'
    context_object_name = 'firms'
    paginate_by = 10

    def get_max_count(self):
        print("5")
        return 5


class FilterFirmsView(MenuInf, ListView):
    template_name = 'app/firms_page.html'
    context_object_name = 'firms'
    def get_queryset(self):
        queryset = Firm.objects.filter(
            Q(place__in=self.request.GET.getlist("place"))| 
            Q(productions__in=self.request.GET.getlist("production"))
            )
        return queryset.distinct()
    
class CreateFirm(CreateView):
    form_class = FirmForm
    template_name = 'app/add_firm.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

def add_firm(request):
    if request.method == 'POST':
        form = FirmForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = FirmForm()
    return render(request, 'news/add_firm.html', {'form': form})


class PersonView(ListView):
    model = Person
    template_name = 'app/people_page.html'
    context_object_name = 'people'
    paginate_by = 20
   

class FirmPage(DetailView): 
    template_name = 'app/firm.html'
    context_object_name = 'firm'

    def get_queryset(self):
        return Firm.objects.filter(slug=self.kwargs['slug'])
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['firm'] = self.get_object()
        firm = Firm.objects.annotate(Count('person'))
        for i in firm:
            if i == self.object:
                self.object.count_person = i.person__count
                self.object.save()
                self.object.refresh_from_db()
        return context
    
class PersonPage(DetailView):
    template_name = 'app/person.html'
    context_object_name = 'person'

    def get_queryset(self):
        return Person.objects.filter(slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = self.get_object()
        return context
