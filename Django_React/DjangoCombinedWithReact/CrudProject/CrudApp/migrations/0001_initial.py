# Generated by Django 5.0.2 on 2024-02-27 14:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Username', models.CharField(max_length=60, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('MobileNumber', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
            ],
            options={
                'db_table': 'Admin_table',
            },
        ),
        migrations.CreateModel(
            name='BooksTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=200)),
                ('AuthorOfBook', models.CharField(max_length=200)),
                ('PublishedYear', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Books_Table',
            },
        ),
    ]
