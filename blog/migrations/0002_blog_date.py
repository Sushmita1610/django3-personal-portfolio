# Generated by Django 3.2.3 on 2021-07-11 04:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 11, 4, 1, 55, 97282, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
