from django.contrib.auth.models import User
from django.test import TestCase

from app.forms import (
    FirmForm,
    PersonForm,
    PlaceForm,
    ProductionForm,
    UserLoginForm,
    UserRegisterForm,
)
from app.models import Firm, Place, Production


class TestForms(TestCase):
    def setUp(self):
        self.place1 = Place.objects.create(place="place 1")
        self.prod1 = Production.objects.create(title="prod 1")
        self.firm1 = Firm.objects.create(
            title="fk_firm",
            slug="fk_firm",
            main_inf="some inf",
            photo="photo",
            location="location",
        )
        self.user = User.objects.create_user(
            username="test", email="mail@gmail.com", password="testpassword"
        )

    def test_place_form_valid(self):
        form = PlaceForm(data={"place": "place1"})

        self.assertTrue(form.is_valid())

    def test_place_form_invalid(self):
        form = PlaceForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_production_form_valid(self):
        form = ProductionForm(data={"title": "prod1"})

        self.assertTrue(form.is_valid())

    def test_productions_form_invalid(self):
        form = ProductionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_firm_form_valid(self):
        form = FirmForm(
            data={
                "title": "firm1",
                "main_inf": "some inf",
                "location": "location",
                "place": [self.place1],
                "productions": [self.prod1],
            }
        )
        self.assertTrue(form.is_valid())

    def test_firm_form_invalid(self):
        form = FirmForm(data={"title": "title"})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_person_form_valid(self):
        form = PersonForm(
            data={
                "name": "person1",
                "main_inf": "some inf",
                "age": 10,
                "gender": "m",
                "adress": "adress",
                "nationality": "nat",
                "family_status": "status",
                "profession": "prof",
                "education": "edu",
                "experience": "exp",
                "current_place": self.firm1,
                "telegram": "telegram",
                "viber": "viber",
                "skype": "skype",
                "mail": "mail@gmail.com",
                "phone": "phone",
            }
        )
        self.assertTrue(form.is_valid())

    def test_person_form_invalid(self):
        form = PersonForm(data={"name": "name"})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 12)

    def test_register_form_valid(self):
        form_data = {
            "username": "testuser",
            "email": "email@gmail.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.fields["username"].label, "Имя пользователя")
        self.assertEqual(form.fields["email"].label, "Email")
        self.assertEqual(form.fields["password1"].label, "Пароль")
        self.assertEqual(form.fields["password2"].label, "Подтверждение пароля")

    def test_register_form_invalid(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_login_form_valid(self):
        form_data = {
            "username": "test",
            "password": "testpassword",
        }
        form = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.fields["username"].label, "Имя пользователя")
        self.assertEqual(form.fields["password"].label, "Пароль")

    def test_login_form_invalid(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
