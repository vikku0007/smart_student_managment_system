# Generated by Django 4.0.4 on 2022-06-03 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0011_rename_addres_staff_permanent_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='permanent_address',
        ),
    ]
