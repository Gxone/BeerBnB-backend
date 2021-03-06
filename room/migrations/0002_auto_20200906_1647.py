# Generated by Django 3.1 on 2020-09-06 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthSafety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_and_safety', models.CharField(max_length=512)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'db_table': 'health_safeties',
            },
        ),
        migrations.CreateModel(
            name='RefundPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_policy', models.CharField(max_length=512)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'db_table': 'refund_policies',
            },
        ),
        migrations.CreateModel(
            name='RuleUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules_of_use', models.CharField(max_length=512)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'db_table': 'rules_of_uses',
            },
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
