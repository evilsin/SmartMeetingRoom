# Generated by Django 2.1.7 on 2019-02-24 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190224_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='room_num',
        ),
    ]
