# Generated by Django 4.1.3 on 2022-11-28 16:06

import birthday.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('web', models.CharField(blank=True, max_length=400, null=True)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('birthday_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('birthday', birthday.fields.BirthdayField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
