# Generated by Django 4.2.17 on 2025-01-12 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_age_alter_user_city_alter_user_county_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='county',
            new_name='country',
        ),
    ]
