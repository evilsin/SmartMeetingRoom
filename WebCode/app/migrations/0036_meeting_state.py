# Generated by Django 2.1.7 on 2019-03-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20190308_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='state',
            field=models.CharField(max_length=4000, null='TRUE'),
            preserve_default='TRUE',
        ),
    ]
