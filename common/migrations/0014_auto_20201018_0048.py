# Generated by Django 3.0.6 on 2020-10-17 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_auto_20201017_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True, verbose_name='В процессе выполнения'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='electrician',
        ),
        migrations.AddField(
            model_name='order',
            name='electrician',
            field=models.ManyToManyField(null=True, related_name='received_orders', to='common.Worker', verbose_name='Члены бригады'),
        ),
        migrations.AlterField(
            model_name='order',
            name='object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='common.Object', verbose_name='Место и наименование проведения работ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_num',
            field=models.CharField(max_length=16, null=True, verbose_name='Номер распоряжения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='common.Organization', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='order',
            name='safety_desc',
            field=models.CharField(max_length=1024, null=True, verbose_name='Технические мероприятия по обеспечению безопасности работ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='subdivision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='common.Subdivision', verbose_name='Подразделение'),
        ),
    ]