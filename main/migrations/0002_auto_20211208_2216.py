# Generated by Django 3.1.7 on 2021-12-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='sex',
        ),
        migrations.AddField(
            model_name='candidate',
            name='vkid',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='vkid'),
        ),
    ]
