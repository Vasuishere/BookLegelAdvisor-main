# Generated by Django 5.1.5 on 2025-02-03 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_lawyer_age'),
        ('userapp', '0044_appointment_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='lid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminapp.lawyer'),
            preserve_default=False,
        ),
    ]
