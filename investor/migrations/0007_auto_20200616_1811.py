# Generated by Django 3.0.7 on 2020-06-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0006_auto_20200616_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invest',
            name='expected_interest',
            field=models.BigIntegerField(),
        ),
    ]
