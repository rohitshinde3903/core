# Generated by Django 5.0.6 on 2024-06-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_students_adress"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cars",
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
                ("CarName", models.CharField(max_length=500)),
                ("Speed", models.IntegerField()),
            ],
        ),
    ]
