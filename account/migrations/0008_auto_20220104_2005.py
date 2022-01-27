# Generated by Django 3.2.6 on 2022-01-04 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='batterytype',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.batterybrand'),
        ),
        migrations.AddField(
            model_name='batterytype',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
