# Generated by Django 2.1.7 on 2019-02-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190227_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='face_id',
            field=models.CharField(default='s', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sname',
            field=models.CharField(default='s', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user_code',
            field=models.CharField(default='s', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user_name',
            field=models.CharField(default='s', max_length=20, null=True),
        ),
    ]
