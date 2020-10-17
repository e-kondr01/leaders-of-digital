# Generated by Django 3.0.6 on 2020-10-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20201017_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='instructions_given',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='instructions_received',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='job_finished',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='job_started',
            field=models.BigIntegerField(null=True),
        ),
    ]
