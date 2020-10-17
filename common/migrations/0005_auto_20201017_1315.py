# Generated by Django 3.0.6 on 2020-10-17 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0004_auto_20201017_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='SafetyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='instructions_given',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='instructions_received',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='job_finished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='job_started',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='workers', to='common.WorkerRole')),
                ('safety_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='workers', to='common.SafetyGroup')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='electrician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='received_orders', to='common.Worker'),
        ),
        migrations.AddField(
            model_name='order',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='given_orders', to='common.Worker'),
        ),
    ]