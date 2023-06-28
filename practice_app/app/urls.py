from django.urls import path

from .views import *

urlpatterns = [
    path('', FirmView.as_view(), name = 'firms_page'),
    path('filter', FilterFirmsView.as_view(), name='filter'),
    path('people', PersonView.as_view(), name = 'people_page'),
    path('firm/<str:slug>/', FirmPage.as_view(), name = 'firm'),
    path('people/<str:slug>/', PersonPage.as_view(), name = 'person'),
    path('add_firm', CreateFirm.as_view(), name = 'add_firm'),
    

]