# Generated by Django 3.0.7 on 2021-03-13 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='data',
            new_name='date',
        ),
    ]
