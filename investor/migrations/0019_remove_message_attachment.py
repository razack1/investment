# Generated by Django 3.0.7 on 2020-06-24 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0018_auto_20200624_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='attachment',
        ),
    ]
