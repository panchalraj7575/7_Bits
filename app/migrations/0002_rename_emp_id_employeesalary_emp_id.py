# Generated by Django 3.2.4 on 2021-06-23 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeesalary',
            old_name='emp_ID',
            new_name='emp_Id',
        ),
    ]