# Generated by Django 3.2.7 on 2021-10-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_auto_20211008_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='GPA',
            field=models.FloatField(default=0.0),
        ),
    ]
