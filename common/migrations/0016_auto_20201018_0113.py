# Generated by Django 3.0.6 on 2020-10-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_auto_20201018_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='electrician',
            field=models.ManyToManyField(related_name='received_orders', to='common.Worker', verbose_name='Члены бригады'),
        ),
    ]
