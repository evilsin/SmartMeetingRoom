# Generated by Django 2.1.7 on 2019-03-01 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_meeting_depart_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='depart_name',
            field=models.CharField(max_length=20, null='False'),
            preserve_default='False',
        ),
    ]
