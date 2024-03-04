# Generated by Django 5.0.2 on 2024-03-02 14:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuthorName', models.CharField(max_length=250)),
                ('BookName', models.CharField(max_length=250)),
                ('BookPublishedOn', models.CharField(max_length=250)),
                ('BookId', models.CharField(max_length=250)),
                ('Status', models.CharField(choices=[('Borrowed', 'Borrowed'), ('Avaliable', 'Avaliable')], max_length=10)),
            ],
            options={
                'db_table': 'Book_Table',
            },
        ),
        migrations.CreateModel(
            name='LibrarianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='firstname must string and should not be less than 3 and greater than 12', regex='^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Lastname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='lastname must string and should not be less than 3 and greater than 12', regex='^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Email', models.EmailField(max_length=50)),
                ('Username', models.CharField(max_length=60, unique=True)),
                ('Password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='password must contain 8 letters and a captail letter and a special character ', regex='^.*(?=.{8,})(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')])),
                ('MobileNumber', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
            ],
            options={
                'db_table': 'Librarian_Table',
            },
        ),
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MemberName', models.CharField(max_length=250)),
                ('MemberId', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('LibraryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LibraryId', to='DjangoSwaggerApp.librarianmodel')),
            ],
            options={
                'db_table': 'Memeber_Table',
            },
        ),
    ]