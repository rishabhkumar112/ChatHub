# Generated by Django 2.1.5 on 2019-01-28 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]