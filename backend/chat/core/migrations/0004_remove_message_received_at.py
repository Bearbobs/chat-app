# Generated by Django 2.0 on 2019-11-21 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180410_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='received_at',
        ),
    ]
