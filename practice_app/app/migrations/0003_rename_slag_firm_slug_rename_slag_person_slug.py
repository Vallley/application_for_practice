# Generated by Django 4.1.7 on 2023-06-23 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_person_options_alter_place_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firm',
            old_name='slag',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='slag',
            new_name='slug',
        ),
    ]
