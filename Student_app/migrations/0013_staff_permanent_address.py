# Generated by Django 4.0.4 on 2022-06-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0012_remove_staff_permanent_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='permanent_address',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
