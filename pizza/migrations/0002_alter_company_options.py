# Generated by Django 4.2.2 on 2023-06-24 10:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pizza", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name": "Company", "verbose_name_plural": "Companies"},
        ),
    ]
