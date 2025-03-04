# Generated by Django 5.1.6 on 2025-02-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_medicine_pharmacies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='pharmacies',
            field=models.ManyToManyField(blank=True, null=True, related_name='medicines', to='pharmacy.pharmacy'),
        ),
    ]
