# Generated by Django 4.1.2 on 2022-11-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mymedcity", "0004_alter_pharmacy_dose"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pharmacy",
            name="dose",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
