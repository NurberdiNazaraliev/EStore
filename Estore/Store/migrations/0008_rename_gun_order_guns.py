# Generated by Django 5.0.1 on 2024-02-06 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_remove_order_guns_order_gun_order_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='gun',
            new_name='guns',
        ),
    ]
