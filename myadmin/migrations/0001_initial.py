# Generated by Django 3.2.7 on 2021-10-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=12)),
                ('adminName', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'adminManagement',
            },
        ),
    ]
