# Generated by Django 4.1.13 on 2024-08-28 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s_mexc', '0007_group_subgroup'),
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
