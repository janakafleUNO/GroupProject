# Generated by Django 3.2.3 on 2022-04-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carviewer', '0003_auto_20220414_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbrand',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='cars/%Y/%M/%D'),
        ),
    ]
