# Generated by Django 2.1.7 on 2019-03-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_auto_20190312_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userinfor',
            name='password',
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='username',
            field=models.CharField(max_length=4096),
        ),
    ]
