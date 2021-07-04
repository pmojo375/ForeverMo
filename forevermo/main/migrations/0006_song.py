# Generated by Django 3.1.4 on 2021-03-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210226_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('artist', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
