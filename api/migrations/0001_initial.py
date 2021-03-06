# Generated by Django 3.2.7 on 2021-09-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('profession', models.CharField(max_length=25)),
                ('profession2', models.CharField(blank=True, max_length=25)),
                ('profession3', models.CharField(blank=True, max_length=25)),
                ('bio', models.TextField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=25)),
                ('location', models.CharField(max_length=25)),
            ],
        ),
    ]
