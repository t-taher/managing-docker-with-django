# Generated by Django 3.1.1 on 2020-09-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_auto_20200922_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='docker',
            name='cotainer_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docker',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='docker',
            name='command',
            field=models.TextField(blank=True, null=True),
        ),
    ]
