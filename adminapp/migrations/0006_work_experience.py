# Generated by Django 5.1.5 on 2025-02-12 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Court', models.CharField(max_length=100)),
                ('Specialization', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='adminapp.lawyer')),
            ],
        ),
    ]
