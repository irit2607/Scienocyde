# Generated by Django 3.1.7 on 2021-03-29 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='last_sub',
            field=models.DateField(default=datetime.date.today),
        ),
    ]