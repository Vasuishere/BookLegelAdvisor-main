# Generated by Django 5.1.4 on 2025-01-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0036_types_law_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='des',
            field=models.TextField(max_length=1500),
        ),
    ]
