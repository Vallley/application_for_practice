from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import FirmView, CreateFirm, register, user_login, user_logout, CreatePerson, CreateProduction, CreatePlace, FilterFirmsView, PersonView, FirmPage, PersonPage 
 
class TestUrls(SimpleTestCase):
    
    def test_firms_page_url_is_resolved(self):
        url = reverse('firms_page')
        self.assertEqual(resolve(url).func.view_class, FirmView)

    def test_filter_url_is_resolved(self):
        url = reverse('filter')
        self.assertEqual(resolve(url).func.view_class, FilterFirmsView)    

    def test_people_page_url_is_resolved(self):
        url = reverse('people_page')
        self.assertEqual(resolve(url).func.view_class, PersonView) 

    def test_firm_url_is_resolved(self):
        url = reverse('firm', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, FirmPage)

    def test_person_url_is_resolved(self):
        url = reverse('person', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, PersonPage)

    def test_add_firm_url_is_resolved(self):
        url = reverse('add_firm')
        self.assertEqual(resolve(url).func.view_class, CreateFirm)    

    def test_add_place_url_is_resolved(self):
        url = reverse('add_place')
        self.assertEqual(resolve(url).func.view_class, CreatePlace)          

    def test_add_production_url_is_resolved(self):
        url = reverse('add_production')
        self.assertEqual(resolve(url).func.view_class, CreateProduction) 

    def test_add_person_url_is_resolved(self):
        url = reverse('add_person')
        self.assertEqual(resolve(url).func.view_class, CreatePerson)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, user_login)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, user_logout)     
