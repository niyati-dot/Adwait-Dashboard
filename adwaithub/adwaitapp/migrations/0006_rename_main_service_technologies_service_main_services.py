# Generated by Django 5.1 on 2024-10-02 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adwaitapp', '0005_rename_main_services_technologies_service_main_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technologies_service',
            old_name='main_service',
            new_name='main_services',
        ),
    ]
