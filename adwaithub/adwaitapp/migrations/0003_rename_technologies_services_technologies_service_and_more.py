# Generated by Django 5.1 on 2024-10-02 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adwaitapp', '0002_portfolio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Technologies_Services',
            new_name='Technologies_Service',
        ),
        migrations.RenameField(
            model_name='technologies_service',
            old_name='main_service',
            new_name='main_services_id',
        ),
        migrations.RenameField(
            model_name='technologies_service',
            old_name='technology',
            new_name='technologies_id',
        ),
    ]