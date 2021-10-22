# Generated by Django 3.2.7 on 2021-10-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_rename_password_adminmanagement_pw'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('pw', models.CharField(auto_created='123456', max_length=12)),
                ('sid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('stuName', models.CharField(max_length=36)),
                ('username', models.CharField(max_length=8)),
                ('gender', models.CharField(max_length=1)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
