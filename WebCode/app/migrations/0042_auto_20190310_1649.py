# Generated by Django 2.1.7 on 2019-03-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_meeting_create_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='depart_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='department',
            name='depart_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
