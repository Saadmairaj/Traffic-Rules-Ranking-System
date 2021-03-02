# Generated by Django 2.2.19 on 2021-03-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('CNG/LPG', 'CNG/LPG'), ('Petrol + CNG', 'Petrol + CNG')], default='Petrol', max_length=20),
            preserve_default=False,
        ),
    ]
