# Generated by Django 4.1.13 on 2024-07-26 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_binance', '0004_proxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='proxy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='s_binance.proxy'),
        ),
        migrations.AddField(
            model_name='group',
            name='proxy_active',
            field=models.BooleanField(default=False),
        ),
    ]
