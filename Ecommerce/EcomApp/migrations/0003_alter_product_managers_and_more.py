# Generated by Django 5.0.1 on 2024-01-08 11:38

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0002_cartitem'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('prod', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='Product',
            new_name='product',
        ),
    ]
