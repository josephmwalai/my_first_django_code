# Generated by Django 5.1.1 on 2024-10-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comrades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comrades',
            name='semester',
            field=models.IntegerField(),
        ),
    ]
