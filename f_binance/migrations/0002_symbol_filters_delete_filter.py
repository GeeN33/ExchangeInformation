# Generated by Django 4.1.13 on 2024-07-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_binance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='symbol',
            name='filters',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Filter',
        ),
    ]
