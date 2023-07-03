from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from app.forms import UserLoginForm, UserRegisterForm
from app.models import Firm, Person, Place, Production


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.firm_url = reverse("firms_page")
        self.people_url = reverse("people_page")
        self.many_to_many_place = Place.objects.create(place="manyplace")
        self.many_to_many_prod = Production.objects.create(title="manyprod")
        self.foreign_key_firm = Firm.objects.create(
            title="fk_firm",
            slug="fk_firm",
            main_inf="some inf",
            photo="photo",
            location="location",
        )
        self.foreign_key_firm.place.add(self.many_to_many_place)
        self.foreign_key_firm.productions.add(self.many_to_many_prod)
        self.person_0 = Person.objects.create(
            name="name0",
            slug="name0",
            main_inf="some inf",
            photo="photo",
            age=10,
            gender="m",
            adress="adress",
            nationality="nat",
            family_status="status",
            profession="prof",
            education="edu",
            experience="exp",
            current_place=self.foreign_key_firm,
            mail="mail",
            phone="phone",
        )
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.user = User.objects.create_user(
            username="user", email="user@gmail.com", password="user123"
        )

    def test_firmview_GET(self):
        number_of_firms = 15
        for firm_num in range(number_of_firms):
            Firm.objects.create(
                title="Firm %s" % firm_num,
                slug="slug %s" % firm_num,
                main_inf="some inf %s" % firm_num,
                photo="photo",
                location="location %s" % firm_num,
            )
        response = self.client.get(self.firm_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/firms_page.html")
        self.assertTrue("is_paginated" in response.context)

    def test_personview_GET(self):
        number_of_people = 21
        for person_num in range(number_of_people):
            Person.objects.create(
                name="Person %s" % person_num,
                slug="slug %s" % person_num,
                main_inf="some inf",
                photo="photo",
                age=10,
                gender="gender",
                adress="adress",
                nationality="nationality",
                family_status="family_status",
                profession="profession",
                education="education",
                experience="experience",
                current_place=self.foreign_key_firm,
                telegram="telegram",
                viber="viber",
                skype="skype",
                mail="mail",
                phone="phone",
            )
        response = self.client.get(self.people_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/people_page.html")
        self.assertTrue("is_paginated" in response.context)

    def test_create_place_POST(self):
        url_place = reverse("add_place")
        response = self.client.post(url_place, {"place": "place1"})
        place1 = Place.objects.get(place="place1")
        self.assertEquals(place1.place, "place1")

    def test_create_production_POST(self):
        url_prod = reverse("add_production")
        response = self.client.post(url_prod, {"title": "prod1"})
        prod1 = Production.objects.get(title="prod1")
        self.assertEquals(prod1.title, "prod1")

    def test_create_firm_POST(self):
        url_firm = reverse("add_firm")
        response = self.client.post(
            url_firm,
            {
                "title": "firm2",
                "main_inf": "some inf",
                "location": "location",
                "productions": self.many_to_many_prod.pk,
                "place": self.many_to_many_place.pk,
            },
        )
        firm2 = Firm.objects.get(title="firm2")
        self.assertEquals(firm2.title, "firm2")
        self.assertEquals(firm2.slug, "firm2")
        self.assertEquals(firm2.main_inf, "some inf")
        self.assertEquals(firm2.location, "location")
        firm2.productions.set([self.many_to_many_prod.pk])
        self.assertEquals(firm2.productions.get(pk=1), self.many_to_many_prod)
        firm2.place.set([self.many_to_many_place.pk])
        self.assertEquals(firm2.place.get(pk=1), self.many_to_many_place)

    def test_create_person_POST(self):
        url_person = reverse("add_person")
        response = self.client.post(
            url_person,
            {
                "name": "person2",
                "main_inf": "some inf",
                "age": 10,
                "gender": "m",
                "adress": "adress",
                "nationality": "nat",
                "family_status": "status",
                "profession": "prof",
                "education": "edu",
                "experience": "exp",
                "current_place": self.foreign_key_firm.pk,
                "mail": "mail@gmail.com",
                "phone": "phone",
            },
        )
        person2 = Person.objects.get(name="person2")
        self.assertEquals(person2.name, "person2")
        self.assertEquals(person2.slug, "person2")
        self.assertEquals(person2.age, 10)
        self.assertEquals(person2.gender, "m")
        self.assertEquals(person2.adress, "adress")
        self.assertEquals(person2.nationality, "nat")
        self.assertEquals(person2.family_status, "status")
        self.assertEquals(person2.profession, "prof")
        self.assertEquals(person2.education, "edu")
        self.assertEquals(person2.experience, "exp")
        self.assertEquals(person2.current_place, self.foreign_key_firm)
        self.assertEquals(person2.mail, "mail@gmail.com")
        self.assertEquals(person2.phone, "phone")

    def test_firm_page_GET(self):
        url_firm_page = reverse("firm", args=["fk_firm"])
        response = self.client.get(url_firm_page)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/firm.html")
        self.assertContains(response, "fk_firm")
        firm = Firm.objects.get(title="fk_firm")
        self.assertEquals(firm.count_person, 1)

    def test_person_page_GET(self):
        url_person_page = reverse("person", args=["name0"])
        response = self.client.get(url_person_page)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/person.html")
        self.assertContains(response, "name0")
        person = Person.objects.get(name="name0")
        self.assertEquals(person.current_place, self.foreign_key_firm)

    def test_filter_firms(self):
        url_filter = reverse("filter")
        response = self.client.get(
            url_filter,
            {
                "productions": [self.many_to_many_prod.pk],
                "place": [self.many_to_many_place.pk],
            },
        )
        queryset = response.context["firms"]
        expected_queryset = Firm.objects.filter(place=self.many_to_many_place)
        self.assertQuerysetEqual(queryset, expected_queryset, transform=lambda x: x)

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/register.html")
        self.assertIsInstance(response.context["form"], UserRegisterForm)

    def test_register_view_post_valid_form(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "test",
                "email": "email@gmail.com",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("firms_page"))
        user = User.objects.get(username="test")
        self.assertEqual(user.username, "test")

    def test_register_view_post_invalid_form(self):
        response = self.client.post(
            self.register_url,
            {
                "username": "",
                "email": "email@gmai.com",
                "password1": "testpassword1",
                "password2": "testpassword2",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/register.html")
        self.assertIsInstance(response.context["form"], UserRegisterForm)
        form = response.context["form"]
        self.assertTrue(form.errors)
        self.assertIn("username", form.errors)
        self.assertIn("password2", form.errors)

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/login.html")
        self.assertIsInstance(response.context["form"], UserLoginForm)

    def test_login_view_valid_form(self):
        response = self.client.post(
            self.login_url, {"username": "user", "password": "user123"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("firms_page"))

    def test_login_view_invalid_form(self):
        response = self.client.post(
            self.login_url,
            {"username": "user", "email": "user@gmail.com", "password": "user12"},
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertTrue(form.errors)
        self.assertIn("__all__", form.errors)

    def test_logout_view_form(self):
        logout_url = reverse("logout")
        response = self.client.post(logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))
