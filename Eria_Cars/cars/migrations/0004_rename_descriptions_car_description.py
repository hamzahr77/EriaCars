# Generated by Django 5.0.1 on 2024-01-27 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='descriptions',
            new_name='description',
        ),
    ]
