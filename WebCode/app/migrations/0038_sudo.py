# Generated by Django 2.1.7 on 2019-03-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20190308_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='sudo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null='False')),
                ('state', models.CharField(max_length=20, null='False')),
            ],
        ),
    ]
