# Generated by Django 3.2.6 on 2022-01-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_employeeregister_availabilty_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(default=500),
        ),
    ]