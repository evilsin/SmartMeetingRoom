# Generated by Django 2.1.7 on 2019-02-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190227_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.CharField(max_length=20, null='False'),
        ),
    ]
