# Generated by Django 5.0.1 on 2024-02-04 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_gun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gun',
            name='caliber',
            field=models.FloatField(),
        ),
    ]