# Generated by Django 5.0.1 on 2024-04-08 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_remove_orderdetail_area"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoggingRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("method", models.CharField(max_length=10)),
                ("path", models.CharField(max_length=255)),
                ("status_code", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="shop.customer",
                    ),
                ),
            ],
        ),
    ]
