from django.urls import path

from . import views

urlpatterns = [
    path('', views.FirmView.as_view(), name = 'firms_page'),
    path('filter', views.FilterFirmsView.as_view(), name='filter'),
    path('people', views.PersonView.as_view(), name = 'people_page'),
    path('firm/<str:slug>/', views.FirmPage.as_view(), name = 'firm'),
    path('people/<str:slug>/', views.PersonPage.as_view(), name = 'person'),
    path('add_firm', views.CreateFirm.as_view(), name = 'add_firm'),
    path('add_place', views.CreatePlace.as_view(), name = 'add_place'),
    path('add_production', views.CreateProduction.as_view(), name = 'add_production'),
    path('add_person', views.CreatePerson.as_view(), name = 'add_person'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]
