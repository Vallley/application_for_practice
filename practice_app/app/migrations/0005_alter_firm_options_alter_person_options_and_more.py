# Generated by Django 4.1.7 on 2023-06-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_person_skype_alter_person_telegram_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firm',
            options={'ordering': ['title'], 'verbose_name': 'Предприятие', 'verbose_name_plural': 'Предприятия'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['place'], 'verbose_name': 'Местоположение', 'verbose_name_plural': 'Местоположения'},
        ),
        migrations.AlterModelOptions(
            name='production',
            options={'ordering': ['title'], 'verbose_name': 'Вид продукции', 'verbose_name_plural': 'Виды продукции'},
        ),
        migrations.AlterField(
            model_name='firm',
            name='location',
            field=models.CharField(max_length=400),
        ),
    ]