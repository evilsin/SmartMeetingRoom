# Generated by Django 2.1.7 on 2019-03-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_remove_meeting_depart_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(max_length=20, null='False'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.DateField(max_length=20, null='False'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.DateField(max_length=20, null='False'),
        ),
    ]
