# Generated by Django 2.1.7 on 2019-03-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_userinfor_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='condition',
            field=models.CharField(default='modify', max_length=20),
        ),
    ]
