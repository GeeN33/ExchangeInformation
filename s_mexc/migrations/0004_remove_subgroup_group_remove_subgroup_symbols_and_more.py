# Generated by Django 4.1.13 on 2024-08-28 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s_mexc', '0003_subgroup_symbols'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='subgroup',
            name='symbols',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='SubGroup',
        ),
    ]
