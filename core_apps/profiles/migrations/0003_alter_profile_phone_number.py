# Generated by Django 4.1.13 on 2023-11-07 20:07

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_alter_profile_about_me_alter_profile_phone_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=30,
                null=True,
                region=None,
                verbose_name="PhoneNumber",
            ),
        ),
    ]