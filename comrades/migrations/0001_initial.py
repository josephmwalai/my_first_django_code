# Generated by Django 5.1.1 on 2024-10-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comrades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('semester', models.IntegerField(max_length=50)),
                ('academic_year', models.IntegerField(max_length=50)),
                ('course', models.CharField(max_length=255)),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=20)),
            ],
        ),
    ]
