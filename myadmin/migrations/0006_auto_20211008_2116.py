# Generated by Django 3.2.7 on 2021-10-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='class_taking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='cp_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='curStatus',
            field=models.IntegerField(default=0),
        ),
    ]
