# Generated by Django 3.1.4 on 2021-08-08 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210808_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='corn',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='foodchoice',
        ),
        migrations.RemoveField(
            model_name='plusone',
            name='corn',
        ),
        migrations.RemoveField(
            model_name='plusone',
            name='foodchoice',
        ),
    ]