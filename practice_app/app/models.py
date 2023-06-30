from django.db import models
from django.urls import reverse


class Production(models.Model):
    title = models.CharField(max_length=250, verbose_name="Вид продукции")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вид продукции"
        verbose_name_plural = "Виды продукции"
        ordering = ["title"]


class Place(models.Model):
    place = models.CharField(max_length=250, verbose_name="Местоположение")

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"
        ordering = ["place"]


class Firm(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    slug = models.SlugField(max_length=250, verbose_name="url", unique=True, blank=True)
    main_inf = models.TextField(verbose_name="Основная информация")
    photo = models.ImageField(upload_to="photos/firm/%Y/%m/%d/", verbose_name="Фото")
    location = models.CharField(max_length=400, verbose_name="Адрес")
    productions = models.ManyToManyField(
        Production, blank=True, related_name="firm", verbose_name="Вид продукции"
    )
    count_person = models.IntegerField(default=0)
    place = models.ManyToManyField(
        Place, blank=True, related_name="firm", verbose_name="Города"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("firm", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"
        ordering = ["title"]


class Person(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    slug = models.SlugField(max_length=250, verbose_name="url", unique=True, blank=True)
    main_inf = models.TextField(verbose_name="Основная информация")
    photo = models.ImageField(upload_to="photos/person/%Y/%m/%d/", verbose_name="Фото")
    age = models.SmallIntegerField(verbose_name="Возраст")
    gender = models.CharField(max_length=100, verbose_name="Пол")
    adress = models.CharField(max_length=300, verbose_name="Адрес")
    nationality = models.CharField(max_length=100, verbose_name="Национальность")
    family_status = models.CharField(max_length=100, verbose_name="Семейный статус")
    profession = models.CharField(max_length=100, verbose_name="Профессия")
    education = models.TextField(verbose_name="Образование")
    experience = models.TextField(verbose_name="Опыт работы")
    current_place = models.ForeignKey(
        Firm,
        on_delete=models.CASCADE,
        related_name="person",
        verbose_name="Настоящее место работы",
    )
    telegram = models.CharField(max_length=100, blank=True)
    viber = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=100, blank=True)
    mail = models.EmailField(max_length=250)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("person", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["name"]
