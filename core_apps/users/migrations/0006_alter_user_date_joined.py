# Generated by Django 4.1.13 on 2023-11-08 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_user_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 8, 13, 22, 26, 922782, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]