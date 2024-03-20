# Generated by Django 5.0.1 on 2024-01-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_page", "0006_backcategory_blogitems_back_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscriber",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
