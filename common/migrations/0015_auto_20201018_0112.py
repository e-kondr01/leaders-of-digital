# Generated by Django 3.0.6 on 2020-10-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20201018_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defect',
            name='report',
        ),
        migrations.AddField(
            model_name='report',
            name='received_at',
            field=models.BigIntegerField(null=True),
        ),
    ]