# Generated by Django 2.1.7 on 2019-03-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_auto_20190310_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='depart_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='depart_num',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
