# Generated by Django 2.1.7 on 2019-02-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20190228_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='depart_num',
        ),
        migrations.AddField(
            model_name='staff',
            name='depart_name',
            field=models.CharField(max_length=20, null='False'),
            preserve_default='False',
        ),
    ]