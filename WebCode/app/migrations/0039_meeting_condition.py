# Generated by Django 2.1.7 on 2019-03-09 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_sudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='condition',
            field=models.CharField(max_length=20, null='False'),
            preserve_default='False',
        ),
    ]
