# Generated by Django 5.0.1 on 2024-01-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=55)),
                ('category', models.CharField(choices=[('Mobile', 'Mobile'), ('Watch', 'Watch'), ('Laptops', 'Laptops')], max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
