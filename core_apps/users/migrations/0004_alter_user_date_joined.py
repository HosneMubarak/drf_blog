# Generated by Django 4.1.13 on 2023-11-07 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 7, 20, 4, 56, 41805, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
