# Generated by Django 2.2.7 on 2019-11-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191122_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='member_emergency',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='member_latitude',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='member_longitude',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='member_msg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='member_tel',
            field=models.CharField(max_length=15),
        ),
    ]
