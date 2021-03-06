# Generated by Django 3.0.6 on 2020-10-17 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_auto_20201018_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='defect',
            name='elimination_time',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='received_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='received_reports', to='common.Worker'),
        ),
    ]
