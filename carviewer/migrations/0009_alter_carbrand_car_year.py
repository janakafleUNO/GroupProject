# Generated by Django 3.2.3 on 2022-03-18 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carviewer', '0008_alter_carmodel_car_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbrand',
            name='car_year',
            field=models.CharField(max_length=50),
        ),
    ]