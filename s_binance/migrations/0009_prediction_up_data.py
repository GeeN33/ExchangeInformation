# Generated by Django 4.1.13 on 2024-08-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_binance', '0008_alter_prediction_predicted_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='up_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
