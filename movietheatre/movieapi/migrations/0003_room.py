# Generated by Django 2.2.6 on 2019-10-26 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0002_auto_20191025_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(max_length=16)),
                ('time', models.DateTimeField()),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapi.Movie')),
            ],
        ),
    ]
