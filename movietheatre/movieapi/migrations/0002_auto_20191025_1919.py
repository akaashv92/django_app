# Generated by Django 2.2.6 on 2019-10-25 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
