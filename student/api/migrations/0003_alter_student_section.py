# Generated by Django 5.0.1 on 2024-01-19 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='api.section'),
        ),
    ]
