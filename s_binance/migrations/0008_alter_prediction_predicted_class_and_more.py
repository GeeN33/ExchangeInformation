# Generated by Django 4.1.13 on 2024-08-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_binance', '0007_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='predicted_class',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='probabilities',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='probability',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
