# Generated by Django 3.2.7 on 2021-10-07 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_rename_admin_adminmanagement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminmanagement',
            old_name='password',
            new_name='pw',
        ),
    ]
