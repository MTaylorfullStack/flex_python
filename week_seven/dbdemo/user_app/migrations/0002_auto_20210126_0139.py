# Generated by Django 2.2 on 2021-01-26 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='last',
        ),
    ]