# Generated by Django 3.1.4 on 2021-02-26 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210226_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='corn',
        ),
        migrations.RemoveField(
            model_name='plusone',
            name='corn',
        ),
    ]
