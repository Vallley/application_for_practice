from django.test import TestCase
from app.models import Production, Place, Firm, Person

class TestModels(TestCase):

    def setUp(self):
        self.place1 = Place.objects.create(place = 'place 1')
        self.prod1 = Production.objects.create(title = 'prod 1')
        self.firm1 = Firm.objects.create(
            title = 'firm 1',
            slug = 'firm-1',
            main_inf = 'some inf',
            location = 'location',)
        self.firm1.place.add(self.place1.pk)
        self.firm1.productions.add(self.prod1.pk)
        self.person1 = Person.objects.create(
            name = 'person 1',
            slug = 'person-1',
            main_inf = 'some inf',
            age = 10,
            gender = 'm',
            nationality = 'nat',
            family_status = 'status',
            profession = 'prof',
            education = 'edu',
            experience = 'exp',
            mail = 'mail@gmail.com',
            phone = 'phone',
            current_place = self.firm1
        )

    def test_place_model(self):
        place = Place.objects.get(place = 'place 1')
        self.assertEquals(place._meta.get_field('place').verbose_name, 'Местоположение')
        self.assertEquals(place._meta.get_field('place').max_length, 250)
        expected_place_name = '%s' % (place.place)
        self.assertEquals(expected_place_name,str(place))

    def test_place_model(self):
        prod = Production.objects.get(title = 'prod 1')
        self.assertEquals(prod._meta.get_field('title').verbose_name, 'Вид продукции')
        self.assertEquals(prod._meta.get_field('title').max_length, 250)
        expected_prod_name = '%s' % (prod.title)
        self.assertEquals(expected_prod_name,str(prod))

    def test_firm_model(self):
        firm = Firm.objects.get(title = 'firm 1')
        self.assertEquals(firm._meta.get_field('title').verbose_name, 'Название')
        self.assertEquals(firm._meta.get_field('title').max_length, 250)
        self.assertEquals(firm._meta.get_field('slug').verbose_name, 'url')
        self.assertEquals(firm._meta.get_field('slug').max_length, 250)
        self.assertEquals(firm._meta.get_field('main_inf').verbose_name, 'Основная информация')
        self.assertEquals(firm._meta.get_field('photo').verbose_name, 'Фото')
        self.assertEquals(firm._meta.get_field('location').verbose_name, 'Адрес')
        self.assertEquals(firm._meta.get_field('location').max_length, 400)
        self.assertEquals(firm._meta.get_field('productions').verbose_name, 'Вид продукции')
        self.assertEquals(firm.productions.get(title = 'prod 1'), self.prod1)
        self.assertEquals(firm.count_person, 0)
        self.assertEquals(firm._meta.get_field('place').verbose_name, 'Города')
        self.assertEquals(firm.place.get(place = 'place 1'), self.place1)
        expected_prod_name = '%s' % (firm.title)
        self.assertEquals(expected_prod_name,str(firm))
        self.assertEqual(firm.get_absolute_url(), '/firm/firm-1/')

    def test_person_model(self):
        person = Person.objects.get(name = 'person 1')
        self.assertEquals(person._meta.get_field('name').verbose_name, 'Имя')
        self.assertEquals(person._meta.get_field('name').max_length, 250)
        self.assertEquals(person._meta.get_field('slug').verbose_name, 'url')
        self.assertEquals(person._meta.get_field('slug').max_length, 250)
        self.assertEquals(person._meta.get_field('main_inf').verbose_name, 'Основная информация')
        self.assertEquals(person._meta.get_field('photo').verbose_name, 'Фото')
        self.assertEquals(person._meta.get_field('age').verbose_name, 'Возраст')
        self.assertEquals(person._meta.get_field('gender').verbose_name, 'Пол')
        self.assertEquals(person._meta.get_field('gender').max_length, 100)
        self.assertEquals(person._meta.get_field('adress').verbose_name, 'Адрес')
        self.assertEquals(person._meta.get_field('adress').max_length, 300)
        self.assertEquals(person._meta.get_field('nationality').verbose_name, 'Национальность')
        self.assertEquals(person._meta.get_field('nationality').max_length, 100)
        self.assertEquals(person._meta.get_field('family_status').verbose_name, 'Семейный статус')
        self.assertEquals(person._meta.get_field('family_status').max_length, 100)
        self.assertEquals(person._meta.get_field('profession').verbose_name, 'Профессия')
        self.assertEquals(person._meta.get_field('profession').max_length, 100)
        self.assertEquals(person._meta.get_field('education').verbose_name, 'Образование')
        self.assertEquals(person._meta.get_field('experience').verbose_name, 'Опыт работы')
        self.assertEquals(person.current_place, self.firm1)
        self.assertEquals(person._meta.get_field('telegram').max_length, 100)
        self.assertEquals(person._meta.get_field('viber').max_length, 100)
        self.assertEquals(person._meta.get_field('skype').max_length, 100)
        self.assertEquals(person._meta.get_field('mail').max_length, 250)
        self.assertEquals(person._meta.get_field('phone').max_length, 100)
        