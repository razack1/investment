# Generated by Django 3.0.7 on 2020-07-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0032_auto_20200709_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editor',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]