# Generated by Django 4.0.4 on 2022-06-03 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0009_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='address',
            new_name='addres',
        ),
    ]
