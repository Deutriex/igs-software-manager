# Generated by Django 2.0.7 on 2022-10-24 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20221024_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_employee_ownership', to='department.Department'),
        ),
    ]
