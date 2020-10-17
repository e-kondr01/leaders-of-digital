# Generated by Django 3.0.6 on 2020-10-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20201017_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='subobject',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='subobject',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
