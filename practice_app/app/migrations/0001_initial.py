# Generated by Django 4.1.7 on 2023-06-22 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slag', models.SlugField(max_length=250, unique=True, verbose_name='url')),
                ('main_inf', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/firm/%Y/%m/%d/')),
                ('location', models.URLField()),
                ('count_person', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slag', models.SlugField(max_length=250, unique=True, verbose_name='url')),
                ('main_inf', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/person/%Y/%m/%d/')),
                ('age', models.SmallIntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=300)),
                ('nationality', models.CharField(max_length=100)),
                ('family_status', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('telegram', models.URLField(blank=True)),
                ('viber', models.URLField(blank=True)),
                ('skype', models.URLField(blank=True)),
                ('mail', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=100)),
                ('current_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='app.firm')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='firm',
            name='place',
            field=models.ManyToManyField(blank=True, related_name='firm', to='app.place'),
        ),
        migrations.AddField(
            model_name='firm',
            name='productions',
            field=models.ManyToManyField(blank=True, related_name='firm', to='app.production'),
        ),
    ]
