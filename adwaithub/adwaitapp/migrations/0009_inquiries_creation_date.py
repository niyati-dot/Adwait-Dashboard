# Generated by Django 5.1 on 2024-11-01 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adwaitapp', '0008_newslettersubscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiries',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
